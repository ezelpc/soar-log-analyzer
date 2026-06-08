from pathlib import Path
from datetime import datetime


def generate_html_report(alerts):

    Path("reports").mkdir(exist_ok=True)

    filename = (
        f"reports/report_"
        f"{datetime.now().strftime('%Y%m%d_%H%M%S')}.html"
    )

    html = """
<!DOCTYPE html>
<html>
<head>
<title>SOAR Report</title>

<style>

body{
    font-family:Arial;
    margin:40px;
}

table{
    border-collapse:collapse;
    width:100%;
}

th,td{
    border:1px solid black;
    padding:8px;
}

</style>

</head>
<body>

<h1>SOAR Incident Report</h1>

<table>

<tr>
<th>User</th>
<th>Attempts</th>
<th>Severity</th>
<th>Technique</th>
<th>MITRE</th>
</tr>
"""

    for alert in alerts:

        html += f"""
<tr>
<td>{alert['user']}</td>
<td>{alert['attempts']}</td>
<td>{alert['severity']}</td>
<td>{alert['technique']}</td>
<td>{alert['mitre_id']}</td>
</tr>
"""

    html += """
</table>

</body>
</html>
"""

    with open(filename, "w", encoding="utf-8") as file:
        file.write(html)

    return filename