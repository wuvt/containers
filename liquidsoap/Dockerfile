FROM debian:bullseye
LABEL maintainer "WUVT IT <it+dockerfiles@wuvt.vt.edu>"

ENV LIQUIDSOAP_VERSION 1.4.1

RUN sed -i 's/$/ non-free/g' /etc/apt/sources.list \
        && apt-get update \
        && apt-get install -y \
            curl festival openssl build-essential autoconf bzip2 \
            m4 perl pkg-config sed sox sudo \
            git \
            ocaml-base-nox \
            ocaml-dune \
            ladspa-sdk \
            libasound2-dev \
            libbiniou-ocaml-dev \
            libcamomile-ocaml-dev \
            libduppy-ocaml-dev \
            libeasy-format-ocaml-dev \
            libfaad-dev \
            libfdk-aac-dev \
            libflac-dev \
            libinotify-ocaml-dev \
            liblo-dev \
            libmad0-dev \
            libmagic-ocaml-dev \
            libmenhir-ocaml-dev \
            libmm-dev \
            libmp3lame-dev \
            libogg-dev \
            libopus-dev \
            libpcre-ocaml-dev \
            libpulse-dev \
            libsamplerate-dev \
            libsedlex-ocaml-dev \
            libshine-dev \
            libsoundtouch-dev \
            libspeex-dev \
            libssl-ocaml-dev \
            libswscale-dev \
            libsyslog-ocaml-dev \
            libtag1-dev \
            libvorbis-dev \
            libxmlm-ocaml-dev \
            libyojson-ocaml-dev \
            menhir \
        && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /usr/src/liquidsoap
WORKDIR /usr/src/liquidsoap

RUN curl --location -O https://github.com/savonet/liquidsoap/releases/download/${LIQUIDSOAP_VERSION}/liquidsoap-${LIQUIDSOAP_VERSION}-full.tar.bz2 \
        && tar -axvf liquidsoap-${LIQUIDSOAP_VERSION}-full.tar.bz2

WORKDIR /usr/src/liquidsoap/liquidsoap-${LIQUIDSOAP_VERSION}-full
COPY PACKAGES .

RUN chown -R nobody:nogroup . \
        && sudo -u nobody ./configure \
        && sudo -u nobody make \
        && make install \
        && rm -rf /usr/src/liquidsoap/liquidsoap-${LIQUIDSOAP_VERSION}-full

WORKDIR /
USER daemon
CMD ["liquidsoap", "--version"]
