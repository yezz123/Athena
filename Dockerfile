# syntax=docker/dockerfile:1

# This Dockerfile uses the following sources:
FROM kalilinux/kali-rolling:latest
FROM python:3.8-slim-buster

# Create Work Dir
WORKDIR /app

# Install apt-utils
RUN apt-get update \
    && apt-get install -y --no-install-recommends apt-utils

# Install Sudo Command
RUN apt-get update \
    && apt-get install -y sudo

# Config sudo to allow no-password sudo for "docker"
RUN adduser --disabled-password --gecos '' docker
RUN adduser docker sudo
RUN echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers

# Set the UID/GID of the docker user
USER docker

# install gnupg
RUN apt-get update \
    && apt-get install -y gnupg \
    && apt-get install -y gnupg2

# this is where I was running into problems with the other approaches
RUN sudo apt-get update

# Preconfigure environment
COPY install.sh /install.sh
RUN sudo ./install.sh


# Copy the Full Project to the container
COPY . /app

# Copy the requirements files to the container and Run pip to install them
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

# Set env vars and Expose ports
ENV PYTHONPATH=/app
EXPOSE 5000 5000
