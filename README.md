# Recruiting Workflow Automation System

An automated applicant tracking and recruiting operations system for small teams built on n8n, Gmail, Google Sheets, and Google Calendar.

## Core Features

- Candidate ingestion and email extraction via Gmail
- Candidate deduplication by Email, Phone, or Name + Role
- Pipeline tracking in Google Sheets:
  `New Application → Screening → Interview → Technical Review → Final Interview → Offer → Hired / Rejected`
- Interview scheduling via Google Calendar
- Hiring manager email alerts and overdue feedback reminders
- Weekly recruiting analytics and time-to-hire metrics
- Human review queue for ambiguous extractions

## Tech Stack

- **Workflow Engine**: n8n (Self-Hosted)
- **Email**: Gmail API
- **State Store**: Google Sheets API
- **Calendar**: Google Calendar API
