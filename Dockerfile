FROM python:3.11.5-slim-bookworm AS base

WORKDIR /app

RUN pip install --upgrade pip==23.1.0
COPY ./requirements.txt .
RUN pip install -r requirements.txt
