ChatGPT Connections, MCP, and Repeat Retrieval
Implementation
The instructor approved ChatGPT as an alternative to Claude Code for the entire assignment. The original exports were collected via ChatGPT connections to Gmail, GitHub, Notion, and Google Calendar.
The project also has a public .mcp.json containing credential-free MCP server URLs for those four services. MCP Inspector testing established that:
- GitHub MCP connected, exposed tools, and successfully fetched this repository's README.md.
- Notion MCP connected and displayed its tools; a completed content retrieval was not confirmed.
- Gmail MCP and Google Calendar MCP have entries in the JSON, but were not independently authenticated or tested.
ChatGPT-connected applications and local MCP servers are different connection methods. Adding a URL to .mcp.json does not authenticate the service.
Exports and repeat retrieval
dataExports/ contains 10 test JSON records per service, organized into four service folders. These are normalized snapshots with metadata, not full native API exports.
repeatExports/2026-10-15/ contains five later metadata search/list results per service (20 total), obtained after the original records. These refer to existing test objects, not newly generated messages/pages/events/repositories. See its RETRIEVAL_LOG.md for search details. An earlier repeat Gmail search is captured in repeat_gmail_retrieval.json.
How to repeat
1. Enable the four relevant ChatGPT service connections.
2. Request test-item retrieval for each service with stable source identifiers and available timestamps.
3. Review results and save each record as UTF-8 JSON in a service-specific directory; preserve original snapshots.
4. Run python3 validate_exports.py to check the required keys and counts.
5. Run python3 server.py and search locally at http://127.0.0.1:8000.
6. For another retrieval, write new records under a dated repeatExports/ folder and document the queries and metadata returned.
This process requires manual file-saving and is not an unattended one-click export. The dashboard searches local files rather than live provider APIs. The current demo video is edited from screenshots, not a continuous live demonstration.
Security
No access tokens should be placed in public .mcp.json or any committed file. Authentication for actual MCP connections must be provided separately. Revoke any tokens previously shown in screenshots or uploads.
