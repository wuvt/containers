FROM debian:stretch

ENV LIQUIDSOAP_VERSION 1.3.2

RUN sed -i 's/$/ non-free/g' /etc/apt/sources.list \
        && apt-get update \
        && apt-get install -y \
            curl festival openssl build-essential autoconf bzip2 \
            m4 perl pkg-config sed sox sudo \
            ocaml-base-nox \
            libalsa-ocaml-dev \
            libbiniou-ocaml-dev \
            libcamomile-ocaml-dev \
            libduppy-ocaml-dev \
            libeasy-format-ocaml-dev \
            libfdk-aac-dev \
            libflac-ocaml-dev \
            libinotify-ocaml-dev \
            libladspa-ocaml-dev \
            liblo-ocaml-dev \
            libmad-ocaml-dev \
            libmagic-ocaml-dev \
            libmm-ocaml-dev \
            libmp3lame-ocaml-dev \
            libogg-ocaml-dev \
            libopus-ocaml-dev \
            libpcre-ocaml-dev \
            libpulse-ocaml-dev \
            libsamplerate-ocaml-dev \
            libsoundtouch-ocaml-dev \
            libspeex-ocaml-dev \
            libswscale-dev \
            libsyslog-ocaml-dev \
            libtaglib-ocaml-dev \
            libvorbis-ocaml-dev \
            libxmlm-ocaml-dev \
            libyojson-ocaml-dev \
        && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /usr/src/liquidsoap
WORKDIR /usr/src/liquidsoap

RUN curl --location -O https://github.com/savonet/liquidsoap/releases/download/${LIQUIDSOAP_VERSION}/liquidsoap-${LIQUIDSOAP_VERSION}-full.tar.gz \
        && tar -axvf liquidsoap-${LIQUIDSOAP_VERSION}-full.tar.gz

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
