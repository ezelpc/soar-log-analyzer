from collections import Counter

from severity import calculate_severity
from attack_mapping import ATTACK_MAPPING


def detect_bruteforce(logs, threshold=5):

    failed_users = []

    for log in logs:

        if "LOGIN_FAILED" in log:

            try:
                user = log.split("user=")[1]
                failed_users.append(user)

            except IndexError:
                continue

    counts = Counter(failed_users)

    alerts = []

    for user, attempts in counts.items():

        if attempts >= threshold:

            mitre = ATTACK_MAPPING["BRUTE_FORCE"]

            alerts.append(
                {
                    "type": "BRUTE_FORCE",
                    "user": user,
                    "attempts": attempts,
                    "severity": calculate_severity(attempts),
                    "mitre_id": mitre["attack_id"],
                    "technique": mitre["technique"],
                    "tactic": mitre["tactic"],
                }
            )

    return alerts