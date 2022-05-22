FROM python:3.8.10

LABEL Author="Cliff Moran"

ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONBUFFERED 1

RUN mkdir /image_repository

WORKDIR /image_repository

# copy code over
COPY ./image_repository /image_repository

# install required packages
RUN pip install -r requirements.txt

RUN chmod +x /image_repository/docker-entrypoint.sh

ENTRYPOINT [ "/image_repository/docker-entrypoint.sh" ]