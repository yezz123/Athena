# syntax=docker/dockerfile:1

# This Dockerfile uses the following sources:
FROM kalilinux/kali-rolling:latest
FROM python:3.8-slim-buster

# Preconfigure environment
COPY install.sh /install.sh
RUN chmod +x /install.sh
RUN ./install.sh

# Create Work Dir
WORKDIR /app

# Copy the Full Project to the container
COPY . /app

# Copy the requirements files to the container and Run pip to install them
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

# Change the working directory to the good Folder
WORKDIR /app/good

ENV PYTHONPATH=/app
EXPOSE 5000 5000
