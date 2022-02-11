FROM python:3.7-slim

RUN python -m pip install --upgrade pip
RUN python -m pip install psycopg2-binary

COPY requirements.txt requirements.txt
RUN python -m pip install -r requirements.txt

COPY . .
