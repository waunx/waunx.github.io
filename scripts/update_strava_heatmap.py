#!/usr/bin/env python3
"""Build a privacy-preserving daily activity summary for the homepage.

The script can read recent activities from the Strava API or a Strava bulk
export CSV. It intentionally discards activity names, exact start times,
coordinates, routes, and activity IDs before writing the public JSON file.
"""

from __future__ import annotations

import argparse
import csv
import json
import math
import os
import stat
import sys
import time
from collections import Counter, defaultdict
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from typing import Any, Iterable, Optional
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen


STRAVA_TOKEN_URL = "https://www.strava.com/oauth/token"
STRAVA_API_BASE = os.environ.get(
    "STRAVA_API_BASE_URL", "https://www.strava.com/api/v3"
).rstrip("/")
DEFAULT_OUTPUT = Path("assets/data/strava-heatmap.json")
WINDOW_DAYS = 371


def _number(value: Any, default: float = 0.0) -> float:
    try:
        parsed = float(value)
        return parsed if math.isfinite(parsed) else default
    except (TypeError, ValueError):
        return default


def _request_json(
    url: str,
    *,
    method: str = "GET",
    data: Optional[dict[str, Any]] = None,
    headers: Optional[dict[str, str]] = None,
    attempts: int = 4,
) -> Any:
    encoded = urlencode(data).encode("utf-8") if data is not None else None
    request = Request(url, data=encoded, headers=headers or {}, method=method)

    for attempt in range(1, attempts + 1):
        try:
            with urlopen(request, timeout=45) as response:
                return json.load(response)
        except HTTPError as exc:
            retryable = exc.code == 429 or 500 <= exc.code < 600
            if not retryable or attempt == attempts:
                message = exc.read().decode("utf-8", errors="replace")
                raise RuntimeError(f"Strava returned HTTP {exc.code}: {message}") from exc
            retry_after = _number(exc.headers.get("Retry-After"), 2**attempt)
            time.sleep(min(max(retry_after, 1), 60))
        except URLError as exc:
            if attempt == attempts:
                raise RuntimeError(f"Could not reach Strava: {exc.reason}") from exc
            time.sleep(2**attempt)

    raise RuntimeError("Strava request failed")


def _refresh_access_token() -> tuple[str, str]:
    required = {
        "STRAVA_CLIENT_ID": os.environ.get("STRAVA_CLIENT_ID", "").strip(),
        "STRAVA_CLIENT_SECRET": os.environ.get("STRAVA_CLIENT_SECRET", "").strip(),
        "STRAVA_REFRESH_TOKEN": os.environ.get("STRAVA_REFRESH_TOKEN", "").strip(),
    }
    missing = [name for name, value in required.items() if not value]
    if missing:
        raise RuntimeError(f"Missing environment variables: {', '.join(missing)}")

    response = _request_json(
        STRAVA_TOKEN_URL,
        method="POST",
        data={
            "client_id": required["STRAVA_CLIENT_ID"],
            "client_secret": required["STRAVA_CLIENT_SECRET"],
            "refresh_token": required["STRAVA_REFRESH_TOKEN"],
            "grant_type": "refresh_token",
        },
    )
    access_token = str(response.get("access_token", "")).strip()
    refresh_token = str(response.get("refresh_token", "")).strip()
    if not access_token or not refresh_token:
        raise RuntimeError("Strava token refresh did not return the expected tokens")
    return access_token, refresh_token


def _save_rotated_refresh_token(refresh_token: str) -> None:
    output_path = os.environ.get("STRAVA_REFRESH_TOKEN_OUT", "").strip()
    if not output_path:
        return

    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(refresh_token, encoding="utf-8")
    path.chmod(stat.S_IRUSR | stat.S_IWUSR)


def _fetch_api_activities(start_date: date) -> list[dict[str, Any]]:
    access_token, refresh_token = _refresh_access_token()
    _save_rotated_refresh_token(refresh_token)

    after = int(datetime.combine(start_date, datetime.min.time(), tzinfo=timezone.utc).timestamp())
    activities: list[dict[str, Any]] = []
    page = 1
    while True:
        query = urlencode({"after": after, "page": page, "per_page": 200})
        batch = _request_json(
            f"{STRAVA_API_BASE}/athlete/activities?{query}",
            headers={"Authorization": f"Bearer {access_token}"},
        )
        if not isinstance(batch, list):
            raise RuntimeError("Unexpected activity response from Strava")
        activities.extend(item for item in batch if isinstance(item, dict))
        if len(batch) < 200:
            break
        page += 1
    return activities


def _parse_date(value: str) -> Optional[date]:
    value = value.strip()
    if not value:
        return None
    if len(value) >= 10 and value[4] == "-" and value[7] == "-":
        try:
            return date.fromisoformat(value[:10])
        except ValueError:
            pass

    formats = (
        "%b %d, %Y, %I:%M:%S %p",
        "%b %d, %Y %I:%M:%S %p",
        "%Y-%m-%d %H:%M:%S",
        "%m/%d/%Y %H:%M",
        "%d/%m/%Y %H:%M",
    )
    for fmt in formats:
        try:
            return datetime.strptime(value, fmt).date()
        except ValueError:
            continue
    return None


def _row_value(row: dict[str, str], *names: str) -> str:
    normalized = {key.strip().lower(): value for key, value in row.items() if key}
    for name in names:
        value = normalized.get(name.lower())
        if value not in (None, ""):
            return value
    return ""


def _load_csv_activities(path: Path, distance_unit: str) -> list[dict[str, Any]]:
    activities: list[dict[str, Any]] = []
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        for row in reader:
            activity_date = _parse_date(
                _row_value(row, "Activity Date", "Start Date", "Date")
            )
            if activity_date is None:
                continue

            distance = _number(_row_value(row, "Distance", "Distance.1"))
            if distance_unit == "km":
                distance *= 1000
            elif distance_unit == "mi":
                distance *= 1609.344

            activities.append(
                {
                    "start_date_local": activity_date.isoformat(),
                    "sport_type": _row_value(row, "Activity Type", "Sport Type", "Type"),
                    "moving_time": _number(
                        _row_value(row, "Moving Time", "Elapsed Time")
                    ),
                    "distance": distance,
                    "total_elevation_gain": _number(
                        _row_value(row, "Elevation Gain", "Total Elevation Gain")
                    ),
                    "suffer_score": _number(
                        _row_value(row, "Relative Effort", "Suffer Score")
                    ),
                }
            )
    return activities


def _friendly_type(raw_type: str) -> str:
    compact = raw_type.replace(" ", "").replace("_", "").lower()
    groups = {
        "Running": {"run", "trailrun", "virtualrun"},
        "Strength": {"weighttraining", "workout", "crossfit"},
        "Cycling": {"ride", "virtualride", "mountainbikeride", "gravelride"},
        "Hiking & Walking": {"hike", "walk"},
        "Swimming": {"swim"},
        "Yoga": {"yoga"},
    }
    for label, types in groups.items():
        if compact in types:
            return label
    return raw_type.strip() or "Other"


def _relative_load(activity: dict[str, Any]) -> float:
    relative_effort = _number(
        activity.get("suffer_score", activity.get("relative_effort"))
    )
    if relative_effort > 0:
        return relative_effort

    minutes = _number(activity.get("moving_time")) / 60
    average_hr = _number(activity.get("average_heartrate"))
    max_hr = _number(activity.get("max_heartrate"))
    if average_hr > 0 and max_hr >= average_hr:
        return minutes * (average_hr / max_hr) ** 2
    return minutes


def _percentile(values: list[float], fraction: float) -> float:
    if not values:
        return 0.0
    position = (len(values) - 1) * fraction
    lower = math.floor(position)
    upper = math.ceil(position)
    if lower == upper:
        return values[lower]
    weight = position - lower
    return values[lower] * (1 - weight) + values[upper] * weight


def _levels(loads: Iterable[float]) -> tuple[list[float], dict[float, int]]:
    ordered = sorted(value for value in loads if value > 0)
    thresholds = [_percentile(ordered, fraction) for fraction in (0.25, 0.5, 0.75)]
    mapping: dict[float, int] = {}
    for value in ordered:
        mapping[value] = 1 + sum(value > threshold for threshold in thresholds)
    return thresholds, mapping


def _build_payload(
    activities: Iterable[dict[str, Any]], start_date: date, end_date: date, source: str
) -> dict[str, Any]:
    daily: dict[str, dict[str, Any]] = defaultdict(
        lambda: {
            "activities": 0,
            "minutes": 0.0,
            "distance_km": 0.0,
            "elevation_m": 0.0,
            "load": 0.0,
            "types": Counter(),
        }
    )

    for activity in activities:
        activity_date = _parse_date(str(activity.get("start_date_local", "")))
        if activity_date is None or not start_date <= activity_date <= end_date:
            continue

        item = daily[activity_date.isoformat()]
        item["activities"] += 1
        item["minutes"] += _number(activity.get("moving_time")) / 60
        item["distance_km"] += _number(activity.get("distance")) / 1000
        item["elevation_m"] += _number(activity.get("total_elevation_gain"))
        item["load"] += _relative_load(activity)
        activity_type = str(activity.get("sport_type") or activity.get("type") or "Other")
        item["types"][_friendly_type(activity_type)] += 1

    _, level_by_load = _levels(item["load"] for item in daily.values())
    days: list[dict[str, Any]] = []
    for day, item in sorted(daily.items()):
        load = round(item["load"], 1)
        days.append(
            {
                "date": day,
                "activities": item["activities"],
                "minutes": round(item["minutes"]),
                "distance_km": round(item["distance_km"], 1),
                "elevation_m": round(item["elevation_m"]),
                "load": load,
                "level": level_by_load.get(item["load"], 1),
                "types": dict(sorted(item["types"].items())),
            }
        )

    total_minutes = sum(item["minutes"] for item in daily.values())
    activity_types: Counter[str] = Counter()
    for item in daily.values():
        activity_types.update(item["types"])

    return {
        "schema_version": 1,
        "generated_at": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "source": source,
        "metric": "Relative daily training load; Strava Relative Effort when available, otherwise moving time.",
        "privacy": "Daily aggregates only; no routes, coordinates, names, timestamps, or activity IDs.",
        "window": {"start": start_date.isoformat(), "end": end_date.isoformat()},
        "summary": {
            "active_days": len(days),
            "activities": sum(item["activities"] for item in daily.values()),
            "hours": round(total_minutes / 60, 1),
            "distance_km": round(sum(item["distance_km"] for item in daily.values()), 1),
            "elevation_m": round(sum(item["elevation_m"] for item in daily.values())),
            "activity_types": dict(sorted(activity_types.items())),
        },
        "days": days,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--csv", type=Path, help="Read a Strava activities.csv export")
    parser.add_argument(
        "--csv-distance-unit",
        choices=("m", "km", "mi"),
        default="km",
        help="Distance unit used by the CSV export (default: km)",
    )
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()

    end_date = date.today()
    start_date = end_date - timedelta(days=WINDOW_DAYS - 1)
    if args.csv:
        activities = _load_csv_activities(args.csv, args.csv_distance_unit)
        source = "Strava export"
    else:
        activities = _fetch_api_activities(start_date)
        source = "Strava API"

    payload = _build_payload(activities, start_date, end_date, source)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(
        f"Wrote {len(payload['days'])} active days and "
        f"{payload['summary']['activities']} activities to {args.output}"
    )
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except RuntimeError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        raise SystemExit(1) from exc
