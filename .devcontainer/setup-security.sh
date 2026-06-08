#!/bin/bash

set -e

echo "[+] Installing Security Tools"

pip install \
bandit \
semgrep \
detect-secrets \
pip-audit \
safety

echo "[✓] Security Tools Ready"