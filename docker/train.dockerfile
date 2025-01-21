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

RUN --mount=type=cache,target=/root/.cache/pip pip install -r requirements.txt --verbose
RUN --mount=type=cache,target=/root/.cache/pip pip install -r requirements_dev.txt --verbose
RUN --mount=type=cache,target=/root/.cache/pip pip install . --no-deps --verbose

ENTRYPOINT ["python", "-u", "src/chromify/train.py"]
