#!/bin/bash

set -e

echo ""
echo "======================================="
echo " CYBERSECURITY DEV ENVIRONMENT"
echo "======================================="
echo ""

bash .devcontainer/setup-git.sh
bash .devcontainer/setup-python.sh
bash .devcontainer/setup-security.sh
bash .devcontainer/setup-tools.sh
bash .devcontainer/setup-project.sh
bash .devcontainer/verify-environment.sh

echo ""
echo "======================================="
echo " ENVIRONMENT READY"
echo "======================================="