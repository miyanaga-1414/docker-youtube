FROM nginx:latest

RUN apt-get -y update \
&& apt-get -y install openssl

RUN rm /etc/nginx/conf.d/default.conf
COPY /nginx/nginx.conf /etc/nginx/conf.d

WORKDIR /var/www/app
