# Third Party Services Data Export

## Purpose
Use ChatGPT to retrieve test data from Gmail, GitHub, Notion, and Google Calendar.

## Export Process
1. Connect to the designated test accounts through ChatGPT.
2. Retrieve at least 10 records from each service.
3. Preserve original content, source IDs, dates, and available metadata.
4. Never invent missing information.
5. Save each record as a UTF-8 JSON file in its correct service folder.

## Folder Structure
- dataExports/gmail/
- dataExports/github/
- dataExports/notion/
- dataExports/google-calendar/

## Validation
Run `python3 validate_exports.py`.

## Dashboard
Run `python3 server.py` and open http://localhost:8000.

## Security
Never store passwords, API keys, or access tokens in the public GitHub repository.

## Limitations
These instructions document the ChatGPT-based workflow approved for the assignment. They do not automatically download or refresh data; exports require running ChatGPT retrieval and saving the returned files.
