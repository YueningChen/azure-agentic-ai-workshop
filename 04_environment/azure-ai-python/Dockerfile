FROM python:3.11-slim

WORKDIR /app

RUN curl -sL https://aka.ms/InstallAzureCLIDeb | bash

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["bash"]
