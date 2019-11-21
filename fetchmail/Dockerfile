FROM alpine:3.10
LABEL maintainer "WUVT IT <it+dockerfiles@wuvt.vt.edu>"

ENV FETCHMAIL_VERSION 6.3.26-r14

RUN apk add --no-cache "fetchmail~${FETCHMAIL_VERSION}"

#USER nobody

CMD ["/usr/bin/fetchmail", "--nodetach", "--nosyslog", "-f", "/etc/fetchmailrc"]
