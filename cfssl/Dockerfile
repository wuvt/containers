FROM alpine:1.12
LABEL maintainer "WUVT IT <it+dockerfiles@wuvt.vt.edu>"

RUN apk add --update curl && rm -rf /var/cache/apk/*

WORKDIR /tmp
COPY SHA256SUMS download.sh /tmp/
RUN chmod +x download.sh && ./download.sh && rm -rf /tmp/*
