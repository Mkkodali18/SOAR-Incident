import json
import os
from datetime import datetime

CASES_FILE = "cases.json"


def _load_cases():
    if not os.path.exists(CASES_FILE):
        return []
    with open(CASES_FILE, "r") as f:
        return json.load(f)


def _write_cases(cases):
    with open(CASES_FILE, "w") as f:
        json.dump(cases, f, indent=2)


def save_case(alert, intel, action):
    cases = _load_cases()

    case = {
        "case_id": len(cases) + 1,
        "timestamp": str(datetime.now()),
        "alert": alert,
        "threat_intel": intel,
        "action": action
    }

    cases.append(case)
    _write_cases(cases)

    return case


def get_cases():
    return _load_cases()
