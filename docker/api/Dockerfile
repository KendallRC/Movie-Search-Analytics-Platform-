FROM python:3.10-alpine

WORKDIR /app

COPY app/ .

RUN pip install -r requirements.txt

RUN ls
RUN python -u tests.py


EXPOSE 5000