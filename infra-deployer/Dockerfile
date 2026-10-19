FROM ghcr.io/opentofu/opentofu:minimal AS tofu
FROM docker.io/alpine/ansible:latest
COPY --from=tofu /usr/local/bin/tofu /usr/local/bin/tofu

ENV INVENTORY="inventory"
ENV PLAYBOOK="main.yml"

RUN mkdir /ansible
VOLUME /ansible

WORKDIR /ansible
CMD ["exec", "ansible-playbook", "-i", "$INVENTORY", "$PLAYBOOK"]
