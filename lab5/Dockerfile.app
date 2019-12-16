FROM python:3.7-alpine
LABEL author="Prometej"

RUN apk update \
    && apk upgrade \
    && apk add git \
    && pip install pipenv

WORKDIR /app

COPY test/requirements.txt ./
RUN pipenv install -r requirements.txt

COPY app/ ./

RUN mkdir /logs

EXPOSE 5000

ENTRYPOINT pipenv run python app.py
