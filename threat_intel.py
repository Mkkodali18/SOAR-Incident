def check_ip_reputation(ip):

    malicious_ips = [
        "192.168.1.100",
        "10.0.0.99"
    ]

    if ip in malicious_ips:
        return {
            "risk_score": 95,
            "status": "Malicious"
        }

    return {
        "risk_score": 10,
        "status": "Safe"
    }