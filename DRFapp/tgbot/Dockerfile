FROM python:3.9-alpine3.16
WORKDIR /tgbot
RUN apk add postgresql-client build-base postgresql-dev
COPY tgbot/requirements.txt .
RUN pip install -r requirements.txt
COPY . .
