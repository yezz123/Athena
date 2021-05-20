# syntax=docker/dockerfile:1
FROM python:3.7-alpine

#create the work dir
WORKDIR /code

#create the env
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

#run the apk add
RUN apk add --no-cache gcc musl-dev linux-headers

#copy the requirements.txt to the docker's dir
COPY requirements.txt requirements.txt

#run the requirements.txt
RUN pip install -r requirements.txt

#run the main files.
EXPOSE 5000
COPY . .
CMD ["flask", "run"]