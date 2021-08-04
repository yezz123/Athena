# syntax=docker/dockerfile:1
# This Dockerfile uses the following sources:
FROM kalilinux/kali-rolling:latest
FROM python:3.8-slim-buster

# Create Work Dir
WORKDIR /app

# Copy the requirements files to the container and Run pip to install them
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

# Copy the Shell script to the container and Run it
COPY install.sh install.sh
RUN sudo ./install.sh

# Copy the Full Project to the container
COPY . /app

# Change the working directory to the good Folder
WORKDIR /app/good

# Run The flask app
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
