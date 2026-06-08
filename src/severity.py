def calculate_severity(attempts):

    if attempts >= 20:
        return "CRITICAL"

    if attempts >= 10:
        return "HIGH"

    if attempts >= 5:
        return "MEDIUM"

    return "LOW"