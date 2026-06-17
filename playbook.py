from datetime import datetime
import json
import os


def block_ip(ip):

    log = f"{datetime.now()} - BLOCKED IP: {ip}\n"

    with open("logs/actions.log", "a") as f:
        f.write(log)

    return {
        "action": "IP Blocked",
        "ip": ip
    }


def create_case(alert, intel, action):

    case = {
        "alert": alert,
        "intel": intel,
        "action": action
    }

    file_path = "cases.json"

    if os.path.exists(file_path):

        with open(file_path, "r") as f:
            cases = json.load(f)

    else:
        cases = []

    cases.append(case)

    with open(file_path, "w") as f:
        json.dump(cases, f, indent=4)

    return case