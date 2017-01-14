FROM debian:jessie-slim

RUN apt-get update && apt-get install -y apt-transport-https

COPY elastic.asc /tmp/
COPY beats.list /etc/apt/sources.list.d/

RUN apt-key add /tmp/elastic.asc \
        && apt-get update \
        && apt-get -y install filebeat

VOLUME "/etc/filebeat"

CMD ["/usr/bin/filebeat", "-c", "/etc/filebeat/filebeat.yml"]
