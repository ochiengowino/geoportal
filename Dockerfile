FROM python:3.11-alpine3.19

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

# Working directory
WORKDIR /geoportal

# Installing Dependencies
COPY ./requirements.txt /geoportal/requirements.txt

RUN pip install virtualenv && virtualenv install --sytem

# Copy project files and directories
COPY . /geoportal/