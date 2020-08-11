#!/bin/bash
if [ "$1" = 'autodump' ]; then
    dest="/data/snapshot_$(date +%Y%m%d).db"
    ETCDCTL_API=3 etcdctl \
        --endpoints "$ETCD_ENDPOINTS" \
        --cert /etc/ssl/etcd/cert.pem \
        --key /etc/ssl/etcd/privkey.pem \
        --cacert /etcd/ssl/etcd/ca.pem \
        snapshot save snapshot_$(date +%Y%m%d).db
    if [ -n "$SFTP_DEST" ]; then
        echo "put \"$dest\"" | sftp -b - \
            -o UserKnownHostsFile=/etc/sshkeys/known_hosts \
            -i /etc/sshkeys/backup "$SFTP_DEST"
        rm -f "$dest"
    fi
else
    exec "$@"
fi

if [[ -n "$HEALTHCHECK_WEBHOOK" ]]; then
    curl -fsS --retry 3 $HEALTHCHECK_WEBHOOK > /dev/null
fi
