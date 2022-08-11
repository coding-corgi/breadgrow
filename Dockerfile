#FROM python:3.9.0
#
##RUN mkdir /root/.ssh/
#
## 이미지를 가지는 사람은 private key 또한 입수 가능
##ADD ./.ssh/id_rsa /root/.ssh/id_rsa
#
##RUN chmod 600 /root/.ssh/id_rsa
#
##RUN touch /root/.ssh/known_hosts
#
##RUN echo "44"
##RUN ssh-keyscan github.com >> /root/.ssh/known_hosts
#
#WORKDIR /home/
#
#RUN echo "6621"
#
##RUN git clone git@github.com:coding-corgi/breadgrow.git
#RUN git clone https://github.com/coding-corgi/breadgrow.git
#
#WORKDIR /home/breadgrow/
#
#RUN pip install -r requirements.txt
#
#RUN pip install gunicorn
#
#RUN pip install mysqlclient
#
#EXPOSE 8000
#
#CMD ["bash","-c", "python manage.py collectstatic --noinput --settings=breadgrow.settings.deploy && python manage.py migrate --settings=breadgrow.settings.deploy && gunicorn breadgrow.wsgi  --env DJANGO_SETTINGS_MODULE=breadgrow.settings.deploy --bind 0.0.0.0:8000"]
#FROM python:3.9.0
#
#
#RUN echo "442"
#
#WORKDIR /home/
#
#
#RUN git clone https://github.com/coding-corgi/breadgrow.git
#
#WORKDIR /home/breadgrow/
#
#RUN pip install -r requirements.txt
#
#RUN pip install gunicorn
#
#RUN pip install mysqlclient
#
#EXPOSE 8000
#
#CMD ["bash","-c", "python manage.py collectstatic --noinput --settings=breadgrow.settings.deploy && python manage.py migrate --settings=breadgrow.settings.deploy && gunicorn breadgrow.wsgi --env DJANGO_SETTINGS_MODULE=breadgrow.settings.deploy --bind 0.0.0.0:8000"]
FROM python:3.9.0

WORKDIR /home/

RUN echo "1635213"

RUN git clone https://github.com/coding-corgi/breadgrow.git

WORKDIR /home/breadgrow/

RUN pip install -r requirements.txt

RUN pip install gunicorn

RUN pip install mysqlclient

EXPOSE 8000

CMD ["bash","-c", "python manage.py collectstatic --noinput --settings=breadgrow.settings.deploy && python manage.py migrate --settings=breadgrow.settings.deploy && gunicorn breadgrow.wsgi  --env DJANGO_SETTINGS_MODULE=breadgrow.settings.deploy --bind 0.0.0.0:8000"]
