# syntax=docker/dockerfile:1

FROM ubuntu:latest

RUN apt-get update -y
RUN apt-get install -y python3-pip python3-dev build-essential

# Create Work Dir
WORKDIR /app

# Copy the Full Project to the container
COPY . /app

# Copy the requirements files to the container and Run pip to install them
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

# Change the working directory to the good Folder
WORKDIR /app/good

# Set env vars and Expose ports
ENV PYTHONPATH=/app
EXPOSE 5000 5000
