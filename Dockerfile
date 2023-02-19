FROM python:3.8-slim-bullseye

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY . .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN shot-scraper install
RUN playwright install-deps

RUN chmod +x ./run.sh
RUN chmod +x ./server/run.sh
RUN chmod +x ./client/run.sh


CMD ./run.sh