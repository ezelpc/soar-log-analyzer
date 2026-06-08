#!/bin/bash

set -e

echo "[+] Installing Python ecosystem"

python -m pip install --upgrade \
pip \
setuptools \
wheel

pip install \
pytest \
pytest-cov \
ruff \
black \
isort \
mypy \
pre-commit \
requests \
httpx \
aiohttp \
rich \
typer \
python-dotenv \
pyyaml \
jinja2 \
stix2 \
taxii2-client \
pymisp

echo "[✓] Python Ready"