FROM python:3.7

LABEL MAINTAINER="zhouwei" email='xiaomao361@163.com'

WORKDIR /home

ADD requirements.txt /home/
RUN pip install -r requirements.txt
ADD ems /home/ems
ADD mysite /home/mysite
ADD manage.py /home/manage.py
ADD static /home/static
ADD db.sqlite3 /home/
RUN mkdir /home/backup

ADD entrypoint.sh /usr/bin/entrypoint.sh

EXPOSE 8000

CMD ["entrypoint.sh"]
