import os
import sys
from pathlib import Path

def validate_environment():
    env_file = Path('.env')
    if not env_file.exists():
        print("[ERROR] .env file not found.")
        return False
    
    required_keys = [
        "RECRUITING_SHEET_ID",
        "GOOGLE_CALENDAR_ID",
        "HIRING_MANAGER_EMAIL",
        "GMAIL_SEARCH_QUERY",
        "N8N_PORT",
        "GENERIC_TIMEZONE"
    ]
    
    env_vars = {}
    with open(env_file, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('#') and '=' in line:
                key, val = line.split('=', 1)
                env_vars[key.strip()] = val.strip()
                
    missing = [k for k in required_keys if k not in env_vars]
    if missing:
        print(f"[ERROR] Missing required keys in .env: {', '.join(missing)}")
        return False
        
    print("[SUCCESS] Environment configuration is valid.")
    return True

if __name__ == '__main__':
    if not validate_environment():
        sys.exit(1)
