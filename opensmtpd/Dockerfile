FROM alpine:edge
LABEL maintainer "WUVT IT <it+dockerfiles@wuvt.vt.edu>"

ENV OPENSMTPD_VERSION 6.6.2p1-r0

RUN apk add --no-cache libressl "opensmtpd~${OPENSMTPD_VERSION}" \
        && install -d -m 711 /var/spool/smtpd

WORKDIR /var/spool/smtpd
EXPOSE 25

CMD ["smtpd", "-dv"]
