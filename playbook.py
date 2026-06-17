from datetime import datetime


def block_ip(ip):

    log = f"{datetime.now()} - BLOCKED IP: {ip}\n"

    with open("logs/actions.log", "a") as f:
        f.write(log)

    return {
        "action": "IP Blocked",
        "ip": ip
    }

  