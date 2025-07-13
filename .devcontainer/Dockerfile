# Use the official Python image from Microsoft devcontainers
FROM mcr.microsoft.com/devcontainers/python:3.12

# Install Azure CLI
RUN curl -sL https://aka.ms/InstallAzureCLIDeb | bash

# COPY Requirements file
COPY requirements.txt /tmp/requirements.txt

# Install Python dependencies
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r /tmp/requirements.txt && rm /tmp/requirements.txt
RUN pip install --no-cache-dir graphrag

# Install Azure Function Core Tools
RUN curl https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > microsoft.gpg && \
    mv microsoft.gpg /etc/apt/trusted.gpg.d/microsoft.gpg && \
    echo "deb [arch=amd64] https://packages.microsoft.com/debian/$(lsb_release -rs 2>/dev/null | cut -d'.' -f 1)/prod $(lsb_release -cs 2>/dev/null) main" > /etc/apt/sources.list.d/azure-functions.list && \
    apt-get update && \
    apt-get install -y azure-functions-core-tools-4
