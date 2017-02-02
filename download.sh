#!/bin/sh

set +e

pkg_url="https://pkg.cfssl.org/R1.2/"
suffix="_linux-amd64"
binaries="
cfssl-bundle
cfssl-certinfo
cfssl-newkey
cfssl-scan
cfssl
cfssljson
mkbundle
multirootca
"

for item in $binaries; do
    curl -O "${pkg_url}${item}${suffix}"
    sha256sum -c SHA256SUMS 2>&1 | grep "${item}${suffix}" | grep OK
    install -D -m0755 "${item}${suffix}" "/usr/bin/${item}"
done
