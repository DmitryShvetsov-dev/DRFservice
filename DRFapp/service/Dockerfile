FROM python:3.9-alpine3.16

WORKDIR /service

RUN apk add postgresql-client build-base postgresql-dev
COPY service/requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8000

RUN adduser --disabled-password service-user

USER service-user

