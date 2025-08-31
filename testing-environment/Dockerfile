FROM ubuntu:24.04
LABEL maintainer="WUVT IT"

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

# Fix potential UTF-8 errors with ansible-test.
RUN locale-gen en_US.UTF-8

COPY initctl_faker .
RUN chmod +x initctl_faker && rm -fr /sbin/initctl && ln -s /initctl_faker /sbin/initctl

# Remove unnecessary getty and udev targets that result in high CPU usage when using
# multiple containers with Molecule (https://github.com/ansible/molecule/issues/1104)
RUN rm -f /lib/systemd/system/systemd*udev* \
  && rm -f /lib/systemd/system/getty.target

RUN useradd -ms testadmin -p $6$3pUhtbFMuy/39TBZ$fqKeTx5JL42Xzwg6g0S850vJ8e/JXX8Ga1qto0fLcoPS1h4NlwX68.5exTiNDM/K2BjCuWDc2dZsWHScl2CHb. -s /bin/bash

# Enable ssh systemd service
RUN ln -s /etc/systemd/system/sshd.service /usr/lib/systemd/system/ssh.service
RUN ln -s /etc/systemd/system/multi-user.target.wants/ssh.service /usr/lib/systemd/system/ssh.service

VOLUME ["/sys/fs/cgroup", "/tmp", "/run"]
EXPOSE 22
CMD ["/lib/systemd/systemd"]
