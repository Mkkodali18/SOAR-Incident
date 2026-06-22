import streamlit as st
import pandas as pd
import json
import os

CASES_FILE = "cases.json"

st.title("SOAR Incident Dashboard")

if not os.path.exists(CASES_FILE):
    st.warning("No cases found yet.")
    st.stop()

with open(CASES_FILE, "r") as f:
    cases = json.load(f)

if len(cases) == 0:
    st.warning("No cases available.")
    st.stop()

df = pd.DataFrame(cases)

total_alerts = len(df)
malicious_alerts = len(df[df["action"].notna()])
safe_alerts = total_alerts - malicious_alerts
blocked_ips = malicious_alerts

st.metric("Total Alerts", total_alerts)
st.metric("Malicious Alerts", malicious_alerts)
st.metric("Safe Alerts", safe_alerts)
st.metric("Blocked IPs", blocked_ips)

severity_counts = {}

for case in cases:
    severity = case["alert"]["severity"]

    if severity in severity_counts:
        severity_counts[severity] += 1
    else:
        severity_counts[severity] = 1

st.subheader("Alerts by Severity")
st.bar_chart(severity_counts)

st.subheader("Incident Cases")
st.dataframe(df)