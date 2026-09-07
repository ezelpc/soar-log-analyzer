# SOAR Log Analyzer

> **Security Operations Automation · Blue Team · MITRE ATT&CK · Incident Response**

SOAR Log Analyzer is a defensive security automation project that turns authentication logs into structured detections, evidence and incident reports. It demonstrates a practical SOC workflow: **ingest → detect → classify → enrich → preserve evidence → notify**.

## 🎯 Portfolio objective

Build a lightweight, reproducible security-operations pipeline for detecting authentication attacks such as brute-force activity and converting raw log data into actionable incident evidence.

## 🔐 Detection workflow

```text
Authentication logs
        ↓
Parser / detection rules
        ↓
Suspicious activity
        ↓
MITRE ATT&CK mapping
        ↓
Severity classification
        ↓
JSON alert + evidence
        ↓
HTML incident report
        ↓
Telegram / Discord notification
```

## 🛡️ Security capabilities

| Capability | Implementation |
|---|---|
| Detection | Brute-force authentication patterns |
| Threat mapping | MITRE ATT&CK T1110 |
| Triage | Severity classification |
| Evidence | Structured JSON artifacts |
| Reporting | HTML incident reports |
| Notification | Telegram + Discord webhooks |
| Reproducibility | Docker / Dev Containers |

## 🧰 Technology stack

- **Language:** Python
- **Security:** MITRE ATT&CK
- **Runtime:** Docker, Dev Containers
- **Automation:** GitHub
- **Integrations:** Telegram API, Discord webhooks

## 📁 Project structure

```text
src/        # detection and automation logic
logs/       # sample authentication logs
alerts/     # generated alert artifacts
reports/    # incident reports
evidence/   # investigation evidence
```

## 🚀 Roadmap

- [ ] FastAPI investigation API
- [ ] TheHive integration
- [ ] Wazuh integration
- [ ] IOC management
- [ ] Threat-intelligence enrichment
- [ ] Automated response playbooks
- [ ] Detection test dataset and regression tests
- [ ] MITRE ATT&CK coverage matrix
- [ ] Containerized CI security checks

## 💼 Why this belongs in a DevSecOps + Cybersecurity portfolio

This project complements infrastructure-focused work by demonstrating the **security operations side of the lifecycle**: detection engineering, evidence handling, incident reporting and response automation.

It is intentionally defensive and designed for controlled lab data.

## 👤 Author

**Ezequiel Perez**  
DevSecOps · Cloud Security · Cybersecurity · Blue Team / SOC
