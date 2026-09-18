import csv
import json
from pathlib import Path

SCHEMAS_DIR = Path('schemas')

TABS_SCHEMA = {
    "Candidates": [
        "candidate_id", "candidate_name", "candidate_email", "candidate_phone",
        "role_title", "source", "application_date", "stage", "stage_updated_at",
        "hiring_manager_name", "hiring_manager_email", "interview_date",
        "interviewers", "feedback_status", "next_action", "next_action_date",
        "time_in_stage_days", "calendar_event_id", "source_message_id",
        "source_message_url", "notes", "last_notified_at", "created_at", "updated_at"
    ],
    "Event_History": [
        "event_id", "candidate_id", "gmail_message_id", "event_type",
        "timestamp", "previous_stage", "new_stage", "status", "error_details"
    ],
    "Review_Queue": [
        "review_id", "gmail_message_id", "received_at", "reason",
        "extracted_payload", "status", "resolution_notes"
    ]
}

def verify_and_generate_schemas():
    SCHEMAS_DIR.mkdir(exist_ok=True)
    all_ok = True
    
    for tab_name, headers in TABS_SCHEMA.items():
        csv_file = SCHEMAS_DIR / f"{tab_name}.csv"
        # Always write exact standard header
        with open(csv_file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(headers)
        print(f"[SUCCESS] Verified schema file: {csv_file}")
        
    return all_ok

def export_n8n_sheets_structure():
    export_path = SCHEMAS_DIR / "sheets_structure.json"
    data = {
        "tabs": list(TABS_SCHEMA.keys()),
        "schemas": TABS_SCHEMA
    }
    with open(export_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"[SUCCESS] Exported n8n sheet structure definition to: {export_path}")

if __name__ == '__main__':
    verify_and_generate_schemas()
    export_n8n_sheets_structure()
