# Second connected-service retrieval — October 15, 2026

On October 15, ChatGPT used the connected Gmail, GitHub, Notion, and Google Calendar services again in a separate conversation context, after the original 40-record snapshot was created. Search/list operations returned five test items from **each of the four services**, for **20 additional provider-backed metadata records**.

- Gmail: `subject:TEST` (five message search summaries).
- GitHub: searched public repositories owned by the project test account (five results).
- Notion: searched `Business Project Ideas`, with additional matching test pages (five results).
- Google Calendar: searched `TEST` events from October 14 through October 31, 2026 (five results).

Each item has its original provider ID and verified title/name plus relevant metadata returned by that service. Separate service directories preserve the same one-JSON-per-item organization as the first export. The original 40 `dataExports/` files have not been modified.

**Scope and limitations:** These are fresh *retrievals of existing test items*, not newly created messages/pages/events/repositories. Gmail entries contain search-result metadata, not entire message bodies. Notion records are page listings rather than full page blocks; GitHub records are repository listings. The process was AI-assisted, not unattended automation. These files were saved from results obtained by ChatGPT, rather than written directly onto the student's Mac by the provider connectors. The earlier demo video is edited, not live screen recording.

Verification: 5 JSON files per service, 20 total, source IDs retained.
