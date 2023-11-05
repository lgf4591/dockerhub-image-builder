FROM debian:latest
LABEL maintainer="LGF"

USER root

RUN mkdir -p /root/code && mkdir -p /root/.ssh
COPY id_rsa* /root/.ssh/
RUN chmod 600 /root/.ssh/id_rsa && chmod 644 /root/.ssh/id_rsa.pub

WORKDIR /root/code


# [Optional] Uncomment this section to install additional OS packages.
RUN apt-get update && export DEBIAN_FRONTEND=noninteractive && apt-get -y install --no-install-recommends git openssh-server net-tools curl wget vim nano



