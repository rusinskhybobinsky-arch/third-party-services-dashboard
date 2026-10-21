
# Third-Party Services Dashboard

**HW3 — Working With Third-Party Services**

## Project Overview

This project demonstrates how AI can retrieve, organize, and search information from multiple third-party services.

The project integrates data from four services:

- Gmail
- GitHub
- Notion
- Google Calendar

ChatGPT was used as an instructor-approved alternative to Claude Code.

## Project Features

- 40 original JSON records across four services
- 20 additional records from a second retrieval
- Organized, service-specific data folders
- Searchable local Python dashboard
- Cross-service search and individual service filtering
- Documented repeatable data-export workflow
- MCP server configuration
- PowerPoint presentation and demonstration video

## How to Run the Dashboard

**Requirements:** Python 3.9 or newer.

1. Download this repository using **Code → Download ZIP**.
2. Extract the ZIP file.
3. Open the extracted project folder containing `server.py`.
4. Open Terminal in that folder.
5. Run the validation script:

   ```bash
   python3 validate_exports.py
   ```

6. Start the dashboard:

   ```bash
   python3 server.py
   ```

7. Open the following address in your browser:

   **http://127.0.0.1:8000**

8. Use the search bar to search across all services, or select an individual service.

To stop the website, return to Terminal and press **Control + C**.

## Project File Structure

| File or Folder | Purpose |
|---|---|
| `dataExports/` | Original exported service data |
| `repeatExports/` | Additional retrieval records |
| `.claude/skills/data-export/SKILL.md` | Repeatable export instructions |
| `.mcp.json` | MCP server configuration |
| `localStorageFormats.md` | Explanation of JSON storage formats |
| `server.py` | Local dashboard application |
| `validate_exports.py` | Data validation script |
| `CHATGPT_CONNECTIONS_AND_REPEAT_EXPORT.md` | Connection and retrieval documentation |
| `third_party_services_presentation.pptx` | Project presentation |
| `third_party_services_demo_final_new.mp4` | Demonstration video |

## MCP and AI Integration

The project includes MCP configuration entries for GitHub, Notion, Gmail, and Google Calendar.

GitHub MCP was used to retrieve repository information, and Notion MCP was connected through MCP Inspector.

ChatGPT's connected applications were used to retrieve test data from all four services.

Authentication credentials are kept outside the public repository.

## Data Storage

Each service has its own subfolder within `dataExports/`. Records are saved as JSON files containing available content, source identifiers, and relevant metadata.

The project also includes additional retrieval records in `repeatExports/`, demonstrating the documented AI-assisted retrieval workflow.

For details about storage formats and retrieval procedures, see `localStorageFormats.md` and `CHATGPT_CONNECTIONS_AND_REPEAT_EXPORT.md`.

## Dashboard Functionality

The dashboard reads locally stored JSON files and allows users to:

- Search data across all four services
- Filter results by a specific service
- View matching records and their available metadata
- Identify the service associated with each result

The dashboard runs locally and does not require paid website hosting.

## Presentation and Demonstration

The project includes a PowerPoint presentation and a demonstration video showing the services, exported data, and dashboard.

All project materials are available in this public GitHub repository.
