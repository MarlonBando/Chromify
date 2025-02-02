# Base image
FROM python:3.11-slim AS base

RUN apt update && \
    apt install --no-install-recommends -y build-essential gcc && \
    apt clean && rm -rf /var/lib/apt/lists/*

WORKDIR /
ENV PYTHONPATH=/


COPY data data/
COPY src/chromify src/chromify
COPY README.md README.md
COPY pyproject.toml pyproject.toml
COPY requirements.txt requirements.txt
COPY requirements_dev.txt requirements_dev.txt

RUN pip install -r requirements.txt --no-cache-dir --verbose
RUN pip install -r requirements_dev.txt --no-cache-dir --verbose
RUN pip install . --no-deps --no-cache-dir --verbose

ENTRYPOINT ["python", "-u", "src/chromify/train.py"]
