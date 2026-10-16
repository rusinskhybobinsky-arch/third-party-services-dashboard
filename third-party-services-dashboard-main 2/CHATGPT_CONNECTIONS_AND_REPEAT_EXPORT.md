# Connections, MCP Testing, and Repeat Retrieval

**HW3 — Third-Party Services Dashboard**

## Implementation

The instructor approved ChatGPT as an alternative to Claude Code. ChatGPT-connected applications were used to retrieve records from Gmail, GitHub, Notion, and Google Calendar. A separate `.mcp.json` lists MCP endpoints for those same four services.

## Verified Connection Status

| Service | Export method | MCP verification |
|---|---|---|
| GitHub | ChatGPT connector | Successfully connected in MCP Inspector and fetched `README.md` |
| Notion | ChatGPT connector | Connected in MCP Inspector; listed tools, search result not confirmed |
| Gmail | ChatGPT connector | MCP address present, authentication not tested |
| Google Calendar | ChatGPT connector | MCP address present, authentication not tested |

A server URL in `.mcp.json` is configuration, not proof of authentication. No private credentials are included.

## Exported Files

| Service | `dataExports/` original JSON | `repeatExports/2026-10-15/` metadata JSON |
|---|---:|---:|
| Gmail | 10 | 5 |
| GitHub | 10 | 5 |
| Notion | 10 | 5 |
| Google Calendar | 10 | 5 |
| **Total** | **40** | **20** |

The later retrievals reference existing records; they do not represent 20 newly created provider objects. The second retrieval is documented in `repeatExports/2026-10-15/RETRIEVAL_LOG.md`. An earlier five-item Gmail retrieval is also recorded in `repeat_gmail_retrieval.json`.

## Repeatable AI-Assisted Workflow

1. Connect ChatGPT to the four test services.
2. Request provider records, including original IDs, titles and available timestamps.
3. Review results and save one UTF-8 JSON file per retrieved item in the corresponding service directory.
4. Run `python3 validate_exports.py` to check original export structure.
5. Run `python3 server.py` and open **http://127.0.0.1:8000**.
6. For the next retrieval, save results to a dated `repeatExports/` directory without replacing the original snapshots.

The `.claude/skills/data-export/SKILL.md` file documents the same approach. This is an AI-assisted process with explicit file-saving; it is not an unattended automated refresh pipeline. Dashboard queries search local JSON, not live service accounts.

## Source Fidelity

The JSON files are structured snapshots. Some email text was reconstructed from fictional sent test content; Notion content was normalized, and later retrieval records contain provider metadata rather than complete bodies/blocks. Structural validation does not certify complete native API fidelity.

## Demonstration

The presentation includes examples comparing original source content with dashboard records. The ~2:55 demonstration video is a narrated edited walkthrough made from screenshots, not a continuous live login and download capture.

## Security

Keep authentication outside checked-in `.mcp.json`. Never publish API tokens, access tokens, passwords or OAuth client secrets. Previously exposed tokens should be revoked.
