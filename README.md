
# Third-Party Services Dashboard

**HW3 — Working With Third-Party Services**

A local Python dashboard that searches test data exported from Gmail, GitHub, Notion, and Google Calendar.

This project uses ChatGPT-connected applications, as approved by the instructor, and includes additional MCP server configuration and testing.

## Project Overview

| Component | Description |
|---|---|
| Services | Gmail, GitHub, Notion, Google Calendar |
| Original data | 40 JSON records — 10 per service |
| Repeat retrieval | 20 additional metadata records — 5 per service |
| Dashboard | Local Python web application |
| MCP configuration | `.mcp.json` |
| Documentation | README, storage formats, export workflow |
| Presentation | PowerPoint and demonstration video |

## How to Run the Dashboard

1. Download and extract this repository.
2. Open Terminal in the extracted project folder.
3. Validate the data:

   `python3 validate_exports.py`

4. Start the dashboard:

   `python3 server.py`

5. Open **http://127.0.0.1:8000** in your browser.

The dashboard allows users to search all exported records or filter results by service.

## Project Structure

- `dataExports/` — Original JSON records, organized by service.
- `repeatExports/2026-10-15/` — Additional retrieval metadata and retrieval log.
- `server.py` — Searchable local dashboard.
- `validate_exports.py` — Checks export structure.
- `localStorageFormats.md` — Describes JSON formats.
- `.claude/skills/data-export/SKILL.md` — AI-assisted export instructions.
- `.mcp.json` — MCP server endpoint configuration.
- `CHATGPT_CONNECTIONS_AND_REPEAT_EXPORT.md` — Connection and retrieval documentation.
- `third_party_services_presentation.pptx` — Presentation.
- `third_party_services_demo_final.mp4` — Demonstration video.

## MCP Configuration

The `.mcp.json` file lists four service endpoints.

| Service | MCP Testing Status |
|---|---|
| GitHub | Connected; successfully retrieved a repository file |
| Notion | Connected; tools listed |
| Gmail | Configured; MCP connection not independently tested |
| Google Calendar | Configured; MCP connection not independently tested |

The project's original exports were retrieved with ChatGPT-connected applications. MCP server configuration is a separate part of the project.

**Security:** No access tokens or passwords are stored in the public configuration.

## Data Exports

The `dataExports/` folder contains 10 test records for each service.

A second retrieval produced five additional metadata records per service, preserved under `repeatExports/2026-10-15/`.

Records retain source identifiers and available metadata. Some content was reconstructed or normalized from test data, so these are structured snapshots rather than complete, unmodified API responses.

## Repeatable Workflow

The documented workflow uses ChatGPT to retrieve data, saves reviewed JSON files locally, validates their structure, and makes them searchable through the dashboard.

This is an AI-assisted workflow with manual file-saving, not a fully automated export process.

## Demonstration

The repository includes a PowerPoint presentation and an edited demonstration video illustrating the project.

The video is assembled from screenshots rather than a continuous live recording.
