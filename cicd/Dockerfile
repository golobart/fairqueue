# Dockerfile

# FROM directive instructing base image to build upon
# TODO change buster image for python:3.7-alpine about 10 times less size
FROM python:3.6-buster

RUN mkdir -p /opt/app
RUN mkdir -p /opt/app/fairqueue
#RUN mkdir -p /opt/app/django_queue_venv
COPY cicd/start-server.sh /opt/app/
COPY cicd/requirements.txt /opt/app/
#COPY fairqueue/requirements.txt /opt/app/
COPY ./ /opt/app/fairqueue/
#COPY fairqueue /opt/app/fairqueue/
# COPY django_queue_venv /opt/app/django_queue_venv/
WORKDIR /opt/app
RUN pip install -r requirements.txt
#RUN chown -R 1002020000:www-data /opt/app
RUN chown -R www-data:www-data /opt/app

EXPOSE 8000
STOPSIGNAL SIGTERM
USER root
RUN apt-get update && apt-get install -y \
     lynx \
     gettext \
#     python-dev  \
     default-libmysqlclient-dev \
     python3-dev \
    && rm -rf /var/lib/apt/lists/*
CMD ["/opt/app/start-server.sh"]
