#!/bin/bash

set -e

echo "[+] Creating Project Structure"

mkdir -p src
mkdir -p tests
mkdir -p docs
mkdir -p logs
mkdir -p alerts
mkdir -p reports
mkdir -p assets
mkdir -p scripts

touch src/__init__.py
touch tests/__init__.py

if [ ! -f README.md ]; then

cat > README.md << 'EOF'
# SOAR Log Analyzer

Cybersecurity Automation Project

## Features

- Detection
- Automation
- Reporting
- Alerting

EOF

fi

if [ ! -f requirements.txt ]; then
touch requirements.txt
fi

if [ ! -f requirements-dev.txt ]; then

cat > requirements-dev.txt << 'EOF'
pytest
ruff
black
isort
mypy
bandit
semgrep
detect-secrets
pip-audit
safety
EOF

fi

if [ ! -f pyproject.toml ]; then

cat > pyproject.toml << 'EOF'
[tool.ruff]
line-length = 100

[tool.pytest.ini_options]
pythonpath = ["src"]
EOF

fi

if [ ! -f .env.example ]; then

cat > .env.example << 'EOF'
API_KEY=
TOKEN=
CHAT_ID=
EOF

fi

if [ ! -f .gitignore ]; then

cat > .gitignore << 'EOF'
# Python
__pycache__/
*.pyc

# VSCode
.vscode/

# Environment
.env

# Cache
.pytest_cache/
.ruff_cache/
.mypy_cache/

# Reports
reports/*.txt

# Alerts
alerts/*.json

# Logs
*.log
EOF

fi

if [ ! -f logs/auth.log ]; then

cat > logs/auth.log << 'EOF'
2026-06-07 LOGIN_SUCCESS user=admin
2026-06-07 LOGIN_FAILED user=admin
2026-06-07 LOGIN_FAILED user=admin
2026-06-07 LOGIN_FAILED user=admin
2026-06-07 LOGIN_FAILED user=admin
2026-06-07 LOGIN_FAILED user=admin
EOF

fi

echo "[✓] Project Ready"