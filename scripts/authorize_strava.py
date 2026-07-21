#!/usr/bin/env python3
"""Authorize the owner's Strava account and save tokens as GitHub secrets."""

from __future__ import annotations

import argparse
import getpass
import json
import secrets
import shutil
import subprocess
import sys
import webbrowser
from http.server import BaseHTTPRequestHandler, HTTPServer
from typing import Any, Optional
from urllib.parse import parse_qs, urlencode, urlparse
from urllib.request import Request, urlopen


TOKEN_URL = "https://www.strava.com/oauth/token"
AUTHORIZE_URL = "https://www.strava.com/oauth/authorize"


class OAuthResult:
    code: Optional[str] = None
    error: Optional[str] = None


def _wait_for_code(client_id: str, port: int) -> str:
    state = secrets.token_urlsafe(24)
    redirect_uri = f"http://localhost:{port}/exchange_token"
    result = OAuthResult()

    class CallbackHandler(BaseHTTPRequestHandler):
        def do_GET(self) -> None:  # noqa: N802 - required by BaseHTTPRequestHandler
            query = parse_qs(urlparse(self.path).query)
            returned_state = query.get("state", [""])[0]
            if returned_state != state:
                result.error = "OAuth state did not match"
            elif query.get("error"):
                result.error = query["error"][0]
            else:
                result.code = query.get("code", [""])[0]

            ok = bool(result.code) and not result.error
            body = (
                "<h2>Strava authorization complete.</h2><p>You can return to the terminal.</p>"
                if ok
                else "<h2>Strava authorization failed.</h2><p>Return to the terminal for details.</p>"
            )
            encoded = ("<!doctype html><meta charset='utf-8'>" + body).encode("utf-8")
            self.send_response(200 if ok else 400)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(encoded)))
            self.end_headers()
            self.wfile.write(encoded)

        def log_message(self, format: str, *args: Any) -> None:
            return

    params = urlencode(
        {
            "client_id": client_id,
            "response_type": "code",
            "redirect_uri": redirect_uri,
            "approval_prompt": "force",
            "scope": "read,activity:read_all",
            "state": state,
        }
    )
    authorization_url = f"{AUTHORIZE_URL}?{params}"
    server = HTTPServer(("127.0.0.1", port), CallbackHandler)
    server.timeout = 300
    print("Opening Strava authorization in your browser…")
    print(f"If it does not open automatically, visit:\n{authorization_url}")
    webbrowser.open(authorization_url)
    server.handle_request()
    server.server_close()

    if result.error:
        raise RuntimeError(result.error)
    if not result.code:
        raise RuntimeError("Timed out waiting for Strava authorization")
    return result.code


def _exchange_code(client_id: str, client_secret: str, code: str) -> dict[str, Any]:
    data = urlencode(
        {
            "client_id": client_id,
            "client_secret": client_secret,
            "code": code,
            "grant_type": "authorization_code",
        }
    ).encode("utf-8")
    request = Request(TOKEN_URL, data=data, method="POST")
    with urlopen(request, timeout=45) as response:
        payload = json.load(response)
    if not payload.get("refresh_token"):
        raise RuntimeError("Strava did not return a refresh token")
    return payload


def _set_github_secret(repository: str, name: str, value: str) -> None:
    subprocess.run(
        ["gh", "secret", "set", name, "--repo", repository],
        input=value + "\n",
        text=True,
        check=True,
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--client-id", required=True, help="Strava application Client ID")
    parser.add_argument("--repo", default="waunx/waunx.github.io")
    parser.add_argument("--port", type=int, default=8765)
    args = parser.parse_args()

    if not shutil.which("gh"):
        raise RuntimeError("GitHub CLI (gh) is required")
    subprocess.run(["gh", "auth", "status"], check=True)

    client_secret = getpass.getpass("Strava Client Secret: ").strip()
    if not client_secret:
        raise RuntimeError("Client Secret cannot be empty")

    code = _wait_for_code(args.client_id, args.port)
    tokens = _exchange_code(args.client_id, client_secret, code)

    print(f"Saving Strava credentials to GitHub Secrets for {args.repo}…")
    _set_github_secret(args.repo, "STRAVA_CLIENT_ID", args.client_id)
    _set_github_secret(args.repo, "STRAVA_CLIENT_SECRET", client_secret)
    _set_github_secret(args.repo, "STRAVA_REFRESH_TOKEN", str(tokens["refresh_token"]))
    print("Strava credentials saved. No token was written to disk or printed.")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:  # keep OAuth/setup failures concise for a one-time tool
        print(f"Error: {exc}", file=sys.stderr)
        raise SystemExit(1) from exc
