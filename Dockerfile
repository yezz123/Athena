# syntax=docker/dockerfile:1
FROM python:3.7-alpine

#create the work dir
WORKDIR /code

#create the env
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

#run the apk add
RUN \
 apk add --no-cache python3 && \
 apk add --no-cache --virtual .build-deps gcc python3-dev musl-dev 

RUN pip install -r requirements.txt
COPY . .

#run the main files.
EXPOSE 5000
CMD ["flask", "run"]