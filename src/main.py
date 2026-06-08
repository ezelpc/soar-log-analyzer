from parser import read_logs
from detector import detect_bruteforce

from alert import (
    save_alerts,
    save_evidence,
    format_alert
)

from report import generate_html_report

from telegram_notifier import send_telegram
from discord_notifier import send_discord


def main():

    print("\nSOAR Analizador de Registros Iniciado\n")

    logs = read_logs("logs/auth.log")

    alerts = detect_bruteforce(logs)

    if not alerts:

        print("No threats detected")

        return

    alert_file = save_alerts(alerts)

    evidence_file = save_evidence(alerts)

    report_file = generate_html_report(alerts)

    for alert in alerts:

        message = format_alert(alert)

        send_telegram(message)

        send_discord(message)

    print("\nDetecciones de amenazas:")
    print("---------------------")

    for alert in alerts:

        print(
            f"{alert['type']} | "
            f"{alert['user']} | "
            f"{alert['severity']}"
        )

    print("\nArchivos Generados")
    print("---------------------")
    print(f"Alertas: {alert_file}")
    print(f"Evidencia: {evidence_file}")
    print(f"Reporte: {report_file}")


if __name__ == "__main__":
    main()