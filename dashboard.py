from datetime import datetime

cases = []


def create_case(alert, intel, action):

    case = {
        "case_id": len(cases) + 1,
        "timestamp": str(datetime.now()),
        "alert": alert,
        "threat_intel": intel,
        "action": action
    }

    cases.append(case)

    return case


