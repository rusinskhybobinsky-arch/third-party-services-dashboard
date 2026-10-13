# Third Party Services Dashboard

Local Python 3.9-compatible searchable dashboard of test data from Gmail, GitHub, Notion, and Google Calendar. All four services have 10 JSON items in `dataExports`.

## Run

In this folder: `python3 server.py`, then open http://127.0.0.1:8000. Stop with Control+C.

To verify: `python3 validate_exports.py`. This checks required keys and counts; it does **not** prove that the exported records perfectly preserve the full provider-native originals.

## Provenance and limits

The metadata identifiers and Calendar dates were checked against connected accounts. Gmail body fields were reconstructed from the exact fictional email content the assistant sent; Notion `content` is normalized from the original authored test pages and was cross-checked against Notion fetch responses. These are human-readable snapshot exports, **not byte-for-byte raw API records**, and Notion's raw block IDs and history are not included. GitHub repository descriptions were authored as test data and may not be GitHub's stored descriptions.

The instructor's Claude Code project skill/.mcp.json requirements must be reconciled with the instructor-approved ChatGPT substitution. Do not fabricate an active MCP configuration. No account tokens or passwords are stored here.
