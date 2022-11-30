ARG TAG=20.04

FROM ubuntu:$TAG

USER root

WORKDIR /app


RUN apt update -y && \
    apt -y install curl --no-install-recommends && \
    rm -rf /var/lib/apt/lists/* && \
    curl -k https://IP


COPY src/ .
ENV DATABASE postgres
RUN rm -rf /bin/bash



USER dev
CMD ["google.com"]
ENTRYPOINT ["/bin/ping"]