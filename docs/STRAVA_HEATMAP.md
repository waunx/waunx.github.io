# Strava heatmap setup

The homepage reads a privacy-preserving activity summary from the `strava-data`
branch. A scheduled GitHub Action refreshes it once per day. The public JSON
contains daily aggregates only; it never includes routes, coordinates, activity
names, exact start times, or Strava activity IDs.

## 1. Create a Strava API application

Strava currently requires a subscription to create an API application. Open
<https://www.strava.com/settings/api>, create an app, and set the authorization
callback domain to `localhost`.

After creating the app, run the one-time authorization helper with its Client
ID. It requests `activity:read_all`, opens Strava's consent page, asks for the
Client Secret without echoing it, and saves the three Strava values directly as
GitHub Secrets:

```bash
python3 scripts/authorize_strava.py --client-id YOUR_CLIENT_ID
```

No token is printed or written to disk.

## 2. Add repository secrets

The authorization helper has already created the first three secrets. Add one
more secret for safe refresh-token rotation:

```bash
gh secret set STRAVA_SECRET_UPDATE_TOKEN --repo waunx/waunx.github.io
```

`STRAVA_SECRET_UPDATE_TOKEN` should be a fine-grained GitHub personal access
token limited to `waunx/waunx.github.io`, with permission to update Actions
secrets. The workflow uses it only to save Strava's rotated refresh token.

## 3. Run the first sync

Open **Actions → Update Strava heatmap → Run workflow**. The workflow creates a
dedicated `strava-data` branch containing `strava-heatmap.json`. The homepage
then loads the aggregate file directly, so a daily site rebuild is unnecessary.

## CSV fallback

If API access is unavailable, download a Strava bulk export and generate the
same public file locally:

```bash
python3 scripts/update_strava_heatmap.py \
  --csv /path/to/activities.csv \
  --csv-distance-unit km \
  --output assets/data/strava-heatmap.json
```

The local file is used as a fallback when the `strava-data` branch is not yet
available.
