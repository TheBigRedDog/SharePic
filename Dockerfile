FROM python:3

LABEL Author="Cliff Moran"

ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONBUFFERED 1

RUN mkdir /image_repository

WORKDIR /image_repository

# copy code over
COPY ./image_directory /image_directory

# install required packages
RUN pip install -r requirements.txt