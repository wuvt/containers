FROM alpine:3.10

ENV OPENSMTPD_VER=6.0.3p1-r3
RUN apk add --no-cache libressl "opensmtpd~${OPENSMTPD_VER}"

VOLUME /var/spool/smtpd
WORKDIR /var/spool/smtpd
EXPOSE 25

CMD ["smtpd", "-dv"]
