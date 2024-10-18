FROM nginx:alpine

RUN mkdir -p /etc/nginx/html/cache && \
    mkdir -p /var/www/html/documentation

ADD nginx.conf /etc/nginx/nginx.conf
ADD documentation/* /var/www/html/documentation/
ADD errors /etc/nginx/errors/errors/