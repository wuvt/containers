FROM peopleperhour/etcdctl:latest
LABEL maintainer "WUVT IT <it+dockerfiles@wuvt.vt.edu>"

RUN apk add --no-cache curl openssh-client

VOLUME /data

COPY docker-entrypoint.sh /

ENTRYPOINT ["/docker-entrypoint.sh"]

CMD ["autodump"]
