FROM mcr.microsoft.com/devcontainers/python:3.12-bookworm

RUN apt-get update && apt-get install -y \
    git \
    curl \
    wget \
    jq \
    tree \
    unzip \
    zip \
    vim \
    nano \
    dnsutils \
    traceroute \
    tcpdump \
    netcat-openbsd \
    nmap \
    whois \
    build-essential \
    make \
    gcc \
    && rm -rf /var/lib/apt/lists/*