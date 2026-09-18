# Setup Guide: Recruiting Workflow Automation System

Quick-start setup guide for local and cloud deployment of the Recruiting Workflow Automation System.

---

## 1. Prerequisites

- [Docker](https://www.docker.com/) & Docker Compose installed.
- A Google Cloud Platform (GCP) project with the following APIs enabled:
  - **Gmail API**
  - **Google Sheets API**
  - **Google Calendar API**
- OAuth 2.0 Credentials (Client ID & Client Secret) created in Google Cloud Console.

---

## 2. Environment Setup

1. Copy `.env.example` to `.env`:
   ```bash
   cp .env.example .env
   ```
2. Open `.env` and fill in your details:
   - `RECRUITING_SHEET_ID`: The ID of your Google Sheet (found in the Google Sheet URL: `https://docs.google.com/spreadsheets/d/<SPREADSHEET_ID>/edit`).
   - `GOOGLE_CALENDAR_ID`: Target Google Calendar ID (e.g. `careers@yourcompany.com` or `primary`).
   - `HIRING_MANAGER_EMAIL`: Email for stage alerts and feedback reminders.
   - `GENERIC_TIMEZONE`: Preferred timezone (e.g., `America/New_York`, `UTC`).

---

## 3. Google Sheets Setup

1. Create a new Google Sheet.
2. Create 3 tabs:
   - `Candidates`
   - `Event_History`
   - `Review_Queue`
3. Import or copy the CSV column headers from the `schemas/` directory:
   - [`schemas/Candidates.csv`](file:///d:/GitHub/New%20folder/Recruiting%20Workflow%20Automation%20System/schemas/Candidates.csv) → header row for `Candidates` tab.
   - [`schemas/Event_History.csv`](file:///d:/GitHub/New%20folder/Recruiting%20Workflow%20Automation%20System/schemas/Event_History.csv) → header row for `Event_History` tab.
   - [`schemas/Review_Queue.csv`](file:///d:/GitHub/New%20folder/Recruiting%20Workflow%20Automation%20System/schemas/Review_Queue.csv) → header row for `Review_Queue` tab.
4. Alternatively, execute the schema initialization script:
   ```bash
   python scripts/init_sheets.py
   ```
5. Validate environment setup:
   ```bash
   python scripts/validate_env.py
   ```

---

## 4. Starting n8n

Run Docker Compose to start the self-hosted n8n container:

```bash
docker compose up -d
```

Access the n8n UI in your browser at `http://localhost:5678`.

---

## 5. Configuring OAuth Credentials in n8n

1. Log into n8n and navigate to **Credentials**.
2. Create a new **Google OAuth2 API** credential.
3. Configure OAuth scopes for:
   - `https://mail.google.com/` (Gmail)
   - `https://www.googleapis.com/auth/spreadsheets` (Google Sheets)
   - `https://www.googleapis.com/auth/calendar` (Google Calendar)
4. Enter your OAuth Client ID & Client Secret from GCP, and authorize the connection.
