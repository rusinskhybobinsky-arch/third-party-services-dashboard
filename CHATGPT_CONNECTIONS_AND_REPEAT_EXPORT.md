# ChatGPT Connections and Repeat Retrieval Evidence

## Implementation choice
The instructor permitted ChatGPT as an alternative to Claude Code. This project used ChatGPT's connected Gmail, GitHub, Notion and Google Calendar applications. Those connections are configured within ChatGPT's account interface, not by a local Claude Code `.mcp.json` file. A fabricated `.mcp.json` would not represent a real functioning connection, so it has intentionally not been added. Confirm with the instructor whether this is an acceptable substitution for the original `.mcp.json` deliverable.

## Repeat retrieval performed on October 13, 2026
After the initial 40-record dataset was assembled, ChatGPT performed another live search of the connected Gmail mailbox with the search query `subject:TEST`, requesting five records. The tool returned five actual message IDs, titles, and provider timestamps. See `repeat_gmail_retrieval.json` for the returned metadata. A separate retrieval of `dataExports/gmail/email-10.json` from the project's GitHub repository verified that the live Gmail ID for `TEST 10 - Project Documentation Checklist` matched the original saved `source_id` (`1a1366bf104322b9`).

This documents a **repeat retrieval from the live connection**, and a check against a saved export. It is **not** a claim that ChatGPT automatically wrote the repeat results into local folders or re-ran a fully automated export pipeline. The original files are preserved; the JSON evidence file is an additional snapshot, not a replacement for the original 40 records.

## Repeatable manual workflow
1. Open ChatGPT with Gmail, GitHub, Notion and Google Calendar connections enabled.
2. Ask ChatGPT to retrieve 10 test items from each connected service, returning source IDs, timestamps, and available metadata. Review the results.
3. Save returned data as UTF-8 JSON in `dataExports/<service>/`, preserving source identifiers and avoiding invented fields. The existing `.claude/skills/data-export/SKILL.md` describes the process.
4. Run `python3 validate_exports.py` to check the local structure; this cannot prove provider-native fidelity.
5. Run `python3 server.py` and search the local data at `http://localhost:8000`.
6. To repeat, run the retrieval request again, compare IDs with earlier exports, and explicitly save the new snapshots.

## Security and limitations
No credentials or access tokens are committed to the public repository. Connected applications may require authorization by the account holder. The original dataset contains human-readable reconstructed/normalized test content; it is not a byte-for-byte provider API export. The demonstration video is edited from screenshots and does not show a continuous live download. Full automation and the original Claude Code MCP configuration have **not** been implemented.
