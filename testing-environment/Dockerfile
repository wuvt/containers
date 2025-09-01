FROM ubuntu:24.04
LABEL maintainer "WUVT IT <it+dockerfiles@wuvt.vt.edu>"

ARG DEBIAN_FRONTEND=noninteractive

# Install dependencies.
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
       software-properties-common \
       rsyslog systemd systemd-cron sudo iproute2 \
       openssh-server \
    && apt-get clean \
    && rm -Rf /var/lib/apt/lists/* \
    && rm -Rf /usr/share/doc && rm -Rf /usr/share/man
RUN sed -i 's/^\($ModLoad imklog\)/#\1/' /etc/rsyslog.conf

COPY initctl_faker .
RUN chmod +x initctl_faker && rm -fr /sbin/initctl && ln -s /initctl_faker /sbin/initctl

# Remove unnecessary getty and udev targets that result in high CPU usage when using
# multiple containers with Molecule (https://github.com/ansible/molecule/issues/1104)
RUN rm -f /lib/systemd/system/systemd*udev* \
  && rm -f /lib/systemd/system/getty.target

RUN useradd -m tadmin -p '$1$BGGb.rYO$FoQmsTiSsKXPMqcm9uvlP1' -s /bin/bash
RUN usermod -aG sudo tadmin

VOLUME ["/sys/fs/cgroup", "/tmp", "/run"]
EXPOSE 22
CMD ["/lib/systemd/systemd"]
