Third Party Services Dashboard
Local searchable dashboard of sample data retrieved from Gmail, GitHub, Notion, and Google Calendar. The instructor approved ChatGPT as an alternative to Claude Code.
Contents
- dataExports/: 10 JSON snapshots per service (40 original records)
- repeatExports/2026-10-15/: 5 additional retrieval-metadata snapshots per service (20 records) and a retrieval log
- server.py: Python local dashboard for searching all four services
- validate_exports.py: validates the original JSON export structure
- .claude/skills/data-export/SKILL.md: documented AI-assisted retrieval procedure
- .mcp.json: credential-free MCP server configuration for GitHub, Notion, Gmail, and Google Calendar
- third_party_services_presentation.pptx: presentation
- third_party_services_demo_final.mp4: demonstration video
Run locally
Run python3 validate_exports.py, then python3 server.py in the project folder. Open http://127.0.0.1:8000 and search all services or filter by one service. Stop the server with Control+C.
Verified MCP functionality
GitHub MCP was connected in MCP Inspector and successfully retrieved this repository's README.md using get_file_contents. Notion MCP was connected and displayed its tools; its completed search result has not been confirmed. Gmail and Google Calendar MCP URLs are configured, but those two MCP connections have not been authenticated or tested. The four services were accessed for exports using instructor-approved ChatGPT connectors.
The public .mcp.json includes endpoint addresses only; it does not contain credentials, and the endpoints require independent authentication in a compatible client.
Data fidelity and project limitations
The JSON records are human-readable snapshots, not raw byte-for-byte service API payloads. Some Gmail body text was reconstructed from fictional messages originally sent; Notion content was normalized from authored test pages. The repeat-export files contain provider-backed metadata rather than complete content. The project skill documents a repeatable assisted process, not an automatic unattended downloader. The demonstration video is an edited presentation, not a continuous live capture of downloading and searching. See localStorageFormats.md, CHATGPT_CONNECTIONS_AND_REPEAT_EXPORT.md, and repeatExports/2026-10-15/RETRIEVAL_LOG.md for detail.
Do not commit any access tokens or passwords to this public repository.
