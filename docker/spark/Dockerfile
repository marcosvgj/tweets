FROM docker.io/bitnami/spark:3-debian-10

USER root
RUN apt update \
    && apt install software-properties-common -y \
    && add-apt-repository ppa:deadsnakes/ppa -y \
    && apt install python3.7

RUN ln -sf /usr/bin/python3.7 /opt/bitnami/python/bin/python3
COPY conf/spark-env.sh conf/spark-env.sh