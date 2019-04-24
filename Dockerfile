FROM python:3.6

RUN apt-get update
RUN apt-get install -y --no-install-recommends \
        libatlas-base-dev gfortran nginx supervisor

RUN pip3 install uwsgi
COPY requirements.txt /project/requirements.txt

RUN pip3 install -r /project/requirements.txt

RUN useradd --no-create-home nginx

RUN rm /etc/nginx/sites-enabled/default
RUN rm -r /root/.cache

COPY ./conf/nginx.conf /etc/nginx/
COPY ./conf/flask-nginx.conf /etc/nginx/conf.d/
COPY ./conf/uwsgi.ini /etc/uwsgi/
COPY ./conf/supervisord.conf /etc/

COPY /app /project/app

WORKDIR /project

EXPOSE 80

CMD ["/usr/bin/supervisord","-n","-loglevel=trace"]

