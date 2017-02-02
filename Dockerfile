FROM golang:1.7-alpine

RUN apk add --update curl && rm -rf /var/cache/apk/*

WORKDIR /tmp
COPY SHA256SUMS download.sh /tmp/
RUN chmod +x download.sh && ./download.sh && rm -rf /tmp/*
