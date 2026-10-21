
# ChatGPT Connections, MCP Setup & Repeat Exports

**HW3 — Third-Party Services Dashboard**

## 1. Project Implementation

This project uses ChatGPT-connected applications to retrieve test data from four services:

- Gmail
- GitHub
- Notion
- Google Calendar

The instructor approved using ChatGPT instead of Claude Code for the assignment.

The repository also includes a `.mcp.json` file containing MCP server endpoints for all four services.

## 2. MCP Connection Status

| Service | MCP Configuration | Verified Functionality |
|---|---|---|
| GitHub | Configured | Connected and retrieved README.md |
| Notion | Configured | Connected and listed available tools |
| Gmail | Configured | Not independently authenticated or tested through MCP |
| Google Calendar | Configured | Not independently authenticated or tested through MCP |

The original data retrieval used ChatGPT's connected applications. These are separate from the MCP servers listed in `.mcp.json`.

MCP authentication credentials are intentionally excluded from the public repository.

## 3. Original Data Exports

The `dataExports/` directory contains 40 JSON snapshots.

| Service | Original Records |
|---|---:|
| Gmail | 10 |
| GitHub | 10 |
| Notion | 10 |
| Google Calendar | 10 |
| **Total** | **40** |

Each service has its own folder. Records contain source identifiers and available metadata.

These files are structured test-data snapshots, not complete unmodified provider API responses. Some content was reconstructed or normalized.

## 4. Repeat Retrieval

A second round of connected-service retrieval was performed on October 15, 2026.

The results are stored in:

`repeatExports/2026-10-15/`

| Service | Additional Records |
|---|---:|
| Gmail | 5 |
| GitHub | 5 |
| Notion | 5 |
| Google Calendar | 5 |
| **Total** | **20** |

The additional records contain metadata retrieved from existing test items rather than newly created records.

The retrieval queries and limitations are documented in `repeatExports/2026-10-15/RETRIEVAL_LOG.md`.

An earlier Gmail retrieval is documented in `repeat_gmail_retrieval.json`.

## 5. Repeatable Export Workflow

1. Open ChatGPT with the four service connections enabled.
2. Retrieve test items, including source IDs, timestamps, and available metadata.
3. Review the returned information.
4. Save the records as UTF-8 JSON files in the appropriate service folders.
5. Run `python3 validate_exports.py` to validate the original export structure.
6. Run `python3 server.py` to launch the local search dashboard.
7. Save future retrievals in dated folders under `repeatExports/`.

The workflow requires manually saving retrieved data. It is not an unattended or one-click automated export process.

## 6. Dashboard

Start the application using:

`python3 server.py`

Open **http://127.0.0.1:8000**.

The dashboard searches the saved local JSON files and supports searching across all services or filtering by individual service.

It does not query the live services when performing a dashboard search.

## 7. Presentation and Demonstration

The repository includes:

- `third_party_services_presentation.pptx`
- `third_party_services_demo_final_new.mp4.`

The demonstration video is a screen recording showing AI-assisted retrieval, exported records, and the locally running dashboard.

## 8. Security

No passwords, API keys, or access tokens should be stored in this public GitHub repository.

MCP services requiring authentication must be authorized separately. Any previously exposed access tokens should be revoked.
