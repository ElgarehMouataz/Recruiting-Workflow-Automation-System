# Workflows Directory

This directory stores exported n8n workflow JSON blueprints for version control and backup.

## Included Workflows

1. **01_candidate_ingestion.json**: Monitors Gmail inbox for candidate applications and parses candidate details.
2. **02_pipeline_upsert.json**: Performs candidate deduplication against Google Sheets and handles status changes.
3. **03_interview_calendar.json**: Manages Google Calendar event creation and interview updates.
4. **04_feedback_reminders.json**: Daily cron job for sending hiring manager alerts when feedback is overdue (>24h).
5. **05_weekly_analytics.json**: Weekly cron job generating recruiting performance summaries and time-to-hire metrics.
6. **06_error_review.json**: Routes extractions with low confidence (< 0.7) to the `Review_Queue` tab.

## Importing Workflows into n8n

1. Open n8n web dashboard (`http://localhost:5678`).
2. Go to **Workflows** → **Import from File**.
3. Select the target `.json` workflow file from this directory.
4. Assign required credentials (Google OAuth2 API / Gmail / Google Sheets / Google Calendar).
