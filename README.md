# SOAR Incident Response Engine

A FastAPI-based SOAR project that automates alert ingestion, threat intelligence enrichment, playbook execution, case management, and RBAC.

## Features

- FastAPI SOAR Listener
- Alert Validation using Pydantic
- Threat Intelligence Enrichment
- Automated Playbook Execution
- IP Blocking Simulation
- Action Logging
- Case Management Dashboard
- Role-Based Access Control (RBAC)

## Run

python -m uvicorn app:app --reload

Alert Source
    ↓
FastAPI API
    ↓
Threat Intel
    ↓
SOAR Playbook
    ↓
Case Store
    ↓
Dashboard