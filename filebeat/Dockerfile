FROM debian:stretch-slim
LABEL maintainer "WUVT IT <it+dockerfiles@wuvt.vt.edu>"

RUN apt-get update && apt-get install -y apt-transport-https gnupg

COPY elastic.asc /tmp/
COPY beats.list /etc/apt/sources.list.d/

RUN apt-key add /tmp/elastic.asc \
        && apt-get update \
        && apt-get -y install filebeat \
        && rm -rf /var/lib/apt/lists/*

VOLUME "/etc/filebeat"

CMD ["/usr/bin/filebeat", "-c", "/etc/filebeat/filebeat.yml"]
