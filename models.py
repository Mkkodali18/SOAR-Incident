from pydantic import BaseModel


class Alert(BaseModel):
    timestamp: str
    source_ip: str
    alert_type: str
    severity: str