# SOAR Incident Response Platform

## Overview

The SOAR Incident Response Platform is a cybersecurity automation project designed to simulate how modern Security Operations Centers (SOC) handle alerts efficiently using Security Orchestration, Automation, and Response (SOAR).

This platform receives security alerts through an API, enriches them using threat intelligence, evaluates risk levels, applies automated response actions, and visualizes incidents through an interactive dashboard.

The project was developed as part of a cybersecurity internship to demonstrate practical SOC automation, incident handling, and security workflow orchestration.

---

## Objectives

* Automate alert ingestion and incident response
* Reduce manual effort for SOC analysts
* Simulate real-world SOAR playbooks
* Improve incident visibility using dashboards
* Demonstrate role-based access control for security operations

---

## Key Features

### Alert Ingestion

Security alerts are received through FastAPI REST endpoints.

### Threat Intelligence Enrichment

Incoming IP addresses are checked against a threat intelligence feed to determine risk scores and malicious reputation.

### Risk Scoring

Each alert is assigned a risk score based on IP reputation.

### Role-Based Access Control (RBAC)

Two analyst roles are supported:

* Junior Analyst
* Senior Analyst

Only Senior Analysts can approve high-risk actions such as blocking malicious IP addresses.

### Automated Response Playbooks

The system performs response actions such as:

* IP blocking
* Incident creation
* Logging actions

### Case Management

All incidents are stored for future analysis and investigation.

### Dashboard Monitoring

A Streamlit dashboard provides:

* Total alerts
* Safe alerts
* Malicious alerts
* Blocked IP count
* Severity charts
* Incident case table

---

## Architecture

```text
Alert Source
    ↓
FastAPI Backend
    ↓
Threat Intelligence Engine
    ↓
Risk Scoring Engine
    ↓
SOAR Playbook Engine
    ↓
Case Management
    ↓
Streamlit Dashboard
```

---

## Project Structure

```text
SOAR-Incident/
│
├── app.py
├── models.py
├── threat_intel.py
├── playbook.py
├── dashboard.py
├── dashboard_ui.py
├── cases.json
├── requirements.txt
├── README.md
├── logs/
└── alerts/
```

---

## Technologies Used

* Python
* FastAPI
* Pydantic
* Streamlit
* Pandas
* Git
* GitHub

---

## Installation

### Clone Repository

```bash
git clone https://github.com/Mkkodali18/SOAR-Incident.git
```

### Move into Project Folder

```bash
cd SOAR-Incident
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Backend

Start FastAPI server:

```bash
python -m uvicorn app:app --reload
```

Open Swagger documentation:

```text
http://127.0.0.1:8000/docs
```

---

## Running the Dashboard

Start Streamlit dashboard:

```bash
python -m streamlit run dashboard_ui.py
```

Dashboard URL:

```text
http://localhost:8501
```

---

## API Endpoints

### POST /alert

Receives security alerts.

Example Request:

```json
{
  "timestamp": "2026-06-22",
  "source_ip": "185.220.101.1",
  "alert_type": "Brute Force",
  "severity": "High"
}
```

---

### GET /cases

Returns all stored incident cases.

---

## Sample Workflow

1. Analyst submits alert
2. API receives alert
3. Threat intelligence checks IP reputation
4. Risk score calculated
5. SOAR playbook executes
6. Malicious IP may be blocked
7. Incident stored in case database
8. Dashboard visualizes incidents

---

## Threat Intelligence Example

Example malicious IPs used for simulation:

* 185.220.101.1
* 45.33.32.156
* 154.35.22.11
* 91.92.109.126

Safe IP examples:

* 8.8.8.8
* 1.1.1.1

---

## Screenshots

Recommended screenshots to add:

* Swagger UI
* Dashboard UI
* GitHub Pull Requests
* Alert execution results

---

## Future Enhancements

* Real threat intelligence API integration
* Database support (SQLite/PostgreSQL)
* User authentication
* CSV/PDF report export
* Email/Slack alerting
* Advanced analytics dashboard

---

## Learning Outcomes

Through this project, I gained practical experience in:

* Security automation
* Incident response workflows
* API development
* Dashboard creation
* Git branching workflows
* Threat intelligence integration

---

## Author

**Mohana Krishna**
Cybersecurity Internship Project
