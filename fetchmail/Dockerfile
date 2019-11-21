FROM alpine:3.10

ENV FETCHMAIL_VER=6.3.26-r14
RUN apk add --no-cache "fetchmail~${FETCHMAIL_VER}"

USER nobody

CMD ["/usr/bin/fetchmail", "-s", "-f", "/etc/fetchmailrc"]
