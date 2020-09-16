FROM python:3.7-slim-buster

RUN apt-get update && apt-get install -y \
    nano

ADD ./requirements.txt app/
WORKDIR /app

RUN pip install -r requirements.txt
