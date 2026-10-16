# Local Storage Formats

All records are UTF-8 JSON objects in `dataExports/<service>/`, one record per file, named with a zero-padded index. The dashboard searches the files, not the live services. Each file has a `service`, `exported_at`, and source-specific fields.

| Service | Data fields | Source identity |
|---|---|---|
| GitHub | `name`, `owner`, `url`, `description`, `visibility`, `default_branch`, `source_id` | Numeric repository ID verified from GitHub |
| Gmail | `subject`, `from`, `to` array, `cc` array, `body`, `thread_id`, `source_id`, `email_ts`, `labels` | Gmail message ID and timestamp verified by Gmail search |
| Notion | `title`, `page_id`, `url`, `content` | Page UUID verified by Notion fetch; content normalized from test-page text |
| Google Calendar | `title`, `description`, `start`, `end`, `timezone`, `calendar_id`, `source_id` | Event ID and start/end verified by Calendar search |

Times are ISO-8601 with offsets. Use null or omit fields where unavailable, never invent provider metadata. `exported_at` indicates when the JSON was assembled, not source creation time. Service identity is conveyed by both folder path and `service` property. `metadata_source` describes how the record was assembled.

**Important:** these are enriched snapshots, not unmodified provider API exports. The validator checks structural sufficiency rather than perfect fidelity; complete raw Notion blocks and original Gmail MIME headers are not captured. This limitation should be disclosed in presentation/submission.
