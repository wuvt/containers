FROM alpine:edge

ENV OPENSMTPD_VER=6.6.1p1-r1
RUN apk add --no-cache libressl "opensmtpd~${OPENSMTPD_VER}"

VOLUME /var/spool/smtpd
WORKDIR /var/spool/smtpd
EXPOSE 25

CMD ["smtpd", "-dv"]
