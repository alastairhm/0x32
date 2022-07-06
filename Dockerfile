FROM ubuntu:21.04 as builder

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get -y upgrade && \
    apt-get -y install git golang && \
    rm -rf /var/lib/apt/lists/*

RUN mkdir /root/src
RUN cd /root/src
RUN git clone https://github.com/gohugoio/hugo.git
RUN cd hugo
RUN go install

ENV HOME /mnt

WORKDIR $HOME
ENTRYPOINT ["/usr/bin/hugo"]

