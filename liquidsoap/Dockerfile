FROM ocaml/opam2:debian-10-ocaml-4.09 as builder

ENV LIQUIDSOAP_VERSION="1.4.3-pre-release"
#ENV EXTRA_PACKAGES="taglib mad lame vorbis cry opus fdkaac faad flac alsa ffmpeg pulseaudio ssl"
ENV EXTRA_PACKAGES="taglib mad lame vorbis cry opus fdkaac faad flac alsa pulseaudio ssl"

RUN opam update \
        && opam upgrade \
        && eval $(opam env)

RUN sudo sed -i 's/$/ non-free/' /etc/apt/sources.list \
        && sudo apt-get update \
        && sudo apt-get install -y autoconf \
        && opam depext -i $EXTRA_PACKAGES
#        && opam depext -i $EXTRA_PACKAGES liquidsoap.${LIQUIDSOAP_VERSION}

RUN eval $(opam config env) \
        && git clone https://github.com/savonet/liquidsoap.git \
        && cd liquidsoap \
        && git checkout v1.4.3-pre-release \
        && opam pin add liquidsoap .

RUN eval $(opam config env) \
        && mkdir -p /home/opam/root/usr/bin \
        && mv $(which liquidsoap) /home/opam/root/usr/bin/ \
        && opam depext -ln $EXTRA_PACKAGES > /home/opam/root/depexts \
        && mkdir -p /home/opam/root/$OPAM_SWITCH_PREFIX/lib \
        && mv $OPAM_SWITCH_PREFIX/share /home/opam/root/$OPAM_SWITCH_PREFIX \
        && mv $OPAM_SWITCH_PREFIX/lib/liquidsoap /home/opam/root/$OPAM_SWITCH_PREFIX/lib

FROM debian:10-slim
LABEL maintainer "WUVT IT <it+dockerfiles@wuvt.vt.edu>"

COPY --from=builder /home/opam/root /

RUN sed -i 's/$/ non-free/' /etc/apt/sources.list \
        && apt-get update \
        && apt-get install curl \
        && cat /depexts | xargs apt-get install -y --no-install-recommends \
        && rm -rf /var/lib/apt/lists/* \
        && liquidsoap --version

WORKDIR /
USER daemon
CMD ["liquidsoap", "--version"]
