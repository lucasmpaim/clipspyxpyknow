FROM python:3.6.6-alpine3.8

MAINTAINER Lucas <lucasmpaim1@gmail.com>

ENV PYTHONUNBUFFERED 1
ENV LC_ALL pt_BR.UTF-8
ENV LANG pt_BR.UTF-8
ENV LANGUAGE pt_BR.UTF-8




RUN apk --no-cache add msttcorefonts-installer fontconfig && \
    update-ms-fonts && \
    fc-cache -f


RUN apk update && \
    apk upgrade && \
    apk add --update-cache --repository http://dl-3.alpinelinux.org/alpine/edge/testing/ \
    py-pip \
    build-base libffi-dev \
    linux-headers jpeg-dev zlib-dev \
    binutils \
    cairo-dev cairo cairo-tools \
    pango-dev pango \
    bash \
    gcc \
    wget \
    unzip && \
    mkdir /app && \
    mkdir /scripts

COPY . /app
COPY ./compose/python/scripts/install_clips.sh /scripts

RUN chmod +x ./scripts/install_clips.sh && ./scripts/install_clips.sh

RUN pip install -Ur ./app/requirements.txt && apk add --update bash && rm -rf /var/cache/apk/*

WORKDIR /app
