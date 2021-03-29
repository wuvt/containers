FROM alpine:3.12 AS builder

ENV ETCD_VER=v3.2.32
ENV GOOGLE_URL=https://storage.googleapis.com/etcd
ENV GITHUB_URL=https://github.com/etcd-io/etcd/releases/download

RUN apk add --no-cache curl 

WORKDIR /build
COPY SHA256SUMS /build/

RUN curl -L ${GITHUB_URL}/${ETCD_VER}/etcd-${ETCD_VER}-linux-amd64.tar.gz -o etcd-${ETCD_VER}-linux-amd64.tar.gz \
        && sha256sum -c SHA256SUMS 2>&1 | grep "etcd-${ETCD_VER}-linux-amd64.tar.gz" | grep OK \
        && tar xzvf etcd-${ETCD_VER}-linux-amd64.tar.gz --strip-components=1

FROM alpine:3.12
LABEL maintainer "WUVT IT <it+dockerfiles@wuvt.vt.edu>"

RUN apk add --no-cache curl openssh-client

VOLUME /data

COPY --from=builder /build/etcdctl /usr/bin/etcdctl
COPY docker-entrypoint.sh /

ENTRYPOINT ["/docker-entrypoint.sh"]

CMD ["autodump"]
