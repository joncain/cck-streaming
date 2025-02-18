# syntax=docker/dockerfile:1
FROM python:3.10-alpine
ARG STREAMKEY

WORKDIR /code
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=8080
ENV STREAMKEY=${STREAMKEY}

RUN apk add --no-cache gcc musl-dev linux-headers
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

EXPOSE 8080

COPY app.py .
CMD ["flask", "run", "--debug"]
