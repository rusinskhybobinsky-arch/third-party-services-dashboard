
---
name: data-export
description: Retrieve third-party service test data and save consistently formatted local JSON snapshots.
---

# Third-Party Services Data Export Skill

## Purpose

Retrieve test data from Gmail, GitHub, Notion, and Google Calendar using the instructor-approved ChatGPT connections. Save each retrieved record as a separate UTF-8 JSON file, preserving source identifiers and available metadata.

## Required Services

- Gmail
- GitHub
- Notion
- Google Calendar

## Export Procedure

1. Connect to the appropriate test account.
2. Retrieve at least five records from each service.
3. Use genuine provider results, preserving the original content when available.
4. Record source IDs, timestamps, and relevant metadata.
5. Do not invent missing fields or reconstruct unavailable content.
6. Save each record separately as a JSON file.
7. Keep the original exports unchanged when conducting another retrieval.

## Storage Structure

Original data:

- `dataExports/gmail/email-01.json`
- `dataExports/github/repo-01.json`
- `dataExports/notion/page-01.json`
- `dataExports/google-calendar/event-01.json`

Later retrievals:

- `repeatExports/YYYY-MM-DD/gmail/`
- `repeatExports/YYYY-MM-DD/github/`
- `repeatExports/YYYY-MM-DD/notion/`
- `repeatExports/YYYY-MM-DD/google-calendar/`

## Required Metadata

| Service | Fields to Preserve |
|---|---|
| Gmail | Message ID, subject, sender, recipient, timestamp, available body |
| GitHub | Repository ID, name, owner, URL, available description |
| Notion | Page ID, title, URL, available page content |
| Google Calendar | Event ID, title, start, end, timezone, calendar ID |

If a field is unavailable, document that limitation instead of inventing it.

## Repeat Retrieval

In a new conversation:

1. Retrieve at least five records from each connected service.
2. Follow the same JSON formats described in `localStorageFormats.md`.
3. Save results into a new dated `repeatExports/` folder.
4. Preserve original `dataExports/` files.
5. Create a `RETRIEVAL_LOG.md` documenting the queries, date, record counts, and limitations.
6. Compare saved source IDs with the provider responses.

## Validation

Run:

`python3 validate_exports.py`

Note: The current validator checks the original `dataExports/` structure. Verify repeat exports separately.

## Dashboard

Run:

`python3 server.py`

Open http://127.0.0.1:8000.

## Security

Never commit passwords, API keys, OAuth secrets, or access tokens.

## Execution Limitation

This is a repeatable AI-assisted workflow, not an unattended export program. ChatGPT retrieves provider data, and the returned snapshots must be saved explicitly to local files.
