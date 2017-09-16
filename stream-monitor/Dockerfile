FROM quay.io/wuvt/liquidsoap:latest

USER root

RUN apt-get update \
        && apt-get -y install msmtp \
        && rm -rf /var/lib/apt/lists/*

COPY monitor.liq /etc/liquidsoap/

USER daemon

CMD ["liquidsoap", "/etc/liquidsoap/monitor.liq"]
