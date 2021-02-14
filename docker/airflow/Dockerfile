FROM puckel/docker-airflow:1.10.9

USER root

RUN update-ca-certificates -f \
    && apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y \
    wget \
    git \
    libatlas3-base \
    libopenblas-base \
    && apt-get clean

RUN mkdir -p /usr/share/man/man1
RUN apt-get install -y default-jre

RUN mkdir libs
COPY libs/ libs/
COPY requirements.txt requirements.txt
COPY /dags /usr/local/airflow/dags

RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install libs/*.whl