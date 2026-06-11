from fastapi import FastAPI, Header, HTTPException
from models import Alert
from threat_intel import check_ip_reputation
from playbook import block_ip
from dashboard import create_case, get_cases

app = FastAPI(title="SOAR Engine")


@app.get("/")
def home():
    return {"message": "SOAR Running"}


@app.post("/alert")
def receive_alert(alert: Alert, role: str = Header(default="Junior")):

    intel = check_ip_reputation(alert.source_ip)

    response = {
        "alert": alert.dict(),
        "threat_intel": intel
    }

    action = None

    if intel["risk_score"] > 80:

        if role != "Senior":
            raise HTTPException(
                status_code=403,
                detail="Only Senior Analysts can approve high-risk actions"
            )

        action = block_ip(alert.source_ip)
        response["action_taken"] = action

    create_case(
        alert.dict(),
        intel,
        action
    )

    return response


@app.get("/cases")
def view_cases():
    return get_cases()