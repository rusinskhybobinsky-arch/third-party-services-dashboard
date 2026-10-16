# Third-Party Services Dashboard

**HW3 — Working With Third-Party Services**

A local Python website for searching test data from Gmail, GitHub, Notion, and Google Calendar. This project uses instructor-approved ChatGPT connections, supplemented by MCP Inspector testing.

## At a Glance

| Item | Included |
|---|---|
| Original exports | 40 JSON files: 10 per service |
| Later retrieval evidence | 20 metadata JSON files: 5 per service |
| Dashboard | `server.py` (local Python web application) |
| Export validation | `validate_exports.py` |
| MCP configuration | `.mcp.json` with four official endpoint URLs |
| Project skill | `.claude/skills/data-export/SKILL.md` |
| Deliverables | PowerPoint, demo video, storage documentation |

## Run the Project

1. Download and extract the repository ZIP.
2. Open Terminal in the extracted project directory.
3. Run `python3 validate_exports.py` to validate the original exports.
4. Run `python3 server.py` to start the website.
5. Visit **http://127.0.0.1:8000** and search all four services or select an individual service.
6. Stop the website with **Control+C**.

The website searches JSON files already downloaded locally; it does not request live provider data at search time.

## Data Organization

- `dataExports/gmail/` — 10 email snapshots
- `dataExports/github/` — 10 repository snapshots
- `dataExports/notion/` — 10 page snapshots
- `dataExports/google-calendar/` — 10 event snapshots
- `repeatExports/2026-10-15/` — additional metadata retrievals, 5 per service, with a retrieval log
- `localStorageFormats.md` — field-level schema and source information

## MCP and ChatGPT Connections

| Service | ChatGPT retrieval | MCP Inspector verification |
|---|---|---|
| GitHub | Used | Connected and successfully fetched this repository's README |
| Notion | Used | Connected and listed tools; completed search result not verified |
| Gmail | Used | Endpoint configured; MCP authentication not tested |
| Google Calendar | Used | Endpoint configured; MCP authentication not tested |

The instructor permitted ChatGPT as an alternative to Claude Code. The four MCP endpoint entries in `.mcp.json` do **not** automatically authenticate providers. Credentials must be configured separately in an authorized client and are not stored here.

## Repeat Retrieval and Reproducibility

A later AI-assisted retrieval produced five metadata records per service. Records refer to existing test items. The documented skill describes how to repeat the retrieval, review provider IDs and timestamps, save JSON files, and validate locally. This process requires manual saving rather than a fully unattended export.

See `CHATGPT_CONNECTIONS_AND_REPEAT_EXPORT.md` and `repeatExports/2026-10-15/RETRIEVAL_LOG.md` for the process and limits.

## Presentation and Demonstration

- `third_party_services_presentation.pptx` — nine slides with source-versus-dashboard examples.
- `third_party_services_demo_final.mp4` — approximately 2 minutes 55 seconds; narrated edited demonstration. It is **not** a continuous live login/download recording.

## Data Fidelity and Security

Snapshots contain verified identifiers and selected metadata but are not byte-for-byte complete API responses. Some Gmail body text was reconstructed from the fictional test messages; Notion text was normalized from authored pages; GitHub descriptions may differ from provider-stored content. The validator checks JSON structure and required fields, not complete fidelity. No credentials or private tokens should be committed to this public repo. Revoke any exposed tokens.
