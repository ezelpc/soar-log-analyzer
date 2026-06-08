import requests

from config import DISCORD_WEBHOOK


def send_discord(message):

    if not DISCORD_WEBHOOK:
        return

    payload = {
        "content": message
    }

    try:

        requests.post(
            DISCORD_WEBHOOK,
            json=payload,
            timeout=10
        )

        print("[+] Discord notification sent")

    except Exception as error:

        print(
            f"[ERROR] Discord notification failed: "
            f"{error}"
        )