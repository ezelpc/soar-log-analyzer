import requests

from config import (
    TELEGRAM_TOKEN,
    TELEGRAM_CHAT_ID
)


def send_telegram(message):

    if not TELEGRAM_TOKEN:
        return

    url = (
        f"https://api.telegram.org/bot"
        f"{TELEGRAM_TOKEN}/sendMessage"
    )

    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message
    }

    try:

        requests.post(
            url,
            json=payload,
            timeout=10
        )

        print("[+] Telegram notification sent")

    except Exception as error:

        print(
            f"[ERROR] Telegram notification failed: "
            f"{error}"
        )