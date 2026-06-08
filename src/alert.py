import json
from pathlib import Path
from datetime import datetime


def save_alerts(alerts):

    Path("alerts").mkdir(exist_ok=True)

    filename = (
        f"alerts/alert_"
        f"{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    )

    with open(filename, "w", encoding="utf-8") as file:
        json.dump(
            alerts,
            file,
            indent=4
        )

    return filename


def save_evidence(alerts):

    Path("evidence").mkdir(exist_ok=True)

    filename = (
        f"evidence/incident_"
        f"{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    )

    with open(filename, "w", encoding="utf-8") as file:
        json.dump(
            alerts,
            file,
            indent=4
        )

    return filename


def format_alert(alert):

    return f"""
🚨 SECURITY ALERT

Type: {alert['type']}
User: {alert['user']}
Attempts: {alert['attempts']}
Severity: {alert['severity']}

MITRE ID: {alert['mitre_id']}
Technique: {alert['technique']}
Tactic: {alert['tactic']}
"""