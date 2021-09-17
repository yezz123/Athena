# syntax=docker/dockerfile:1

# This Dockerfile uses the following sources:
FROM kalilinux/kali-rolling:latest
FROM python:3.8-slim-buster


RUN apt-get update \
    && apt-get install -y sudo

RUN adduser --disabled-password --gecos '' docker
RUN adduser docker sudo
RUN echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers

USER docker

# this is where I was running into problems with the other approaches
RUN sudo apt-get update

# Preconfigure environment
COPY install.sh /install.sh
RUN chmod +x /install.sh
RUN sudo ./install.sh

# Create Work Dir
WORKDIR /app

# Copy the Full Project to the container
COPY . /app

# Copy the requirements files to the container and Run pip to install them
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

ENV PYTHONPATH=/app
EXPOSE 5000 5000
