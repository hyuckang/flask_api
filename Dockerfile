FROM ubuntu:16.04

LABEL maintainer="hyuckang15@gmail.com"

RUN apt update && apt install apache2 -y \
python3-pip \
libapache2-mod-wsgi-py3 -y

RUN pip3 install flask
RUN a2enmod wsgi

# apache2 conf, wsgi
COPY ./flask_api_1.conf /etc/apache2/apache2.conf
COPY ./flask_api_2.conf /etc/apache2/sites-available/000-default.conf
COPY ./flask_api.wsgi /var/www/flask_api/flask_api.wsgi

# app
COPY ./app /var/www/flask_api

EXPOSE 80
WORKDIR /var/www/flask_api

CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]
