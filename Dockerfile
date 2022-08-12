FROM python:3.9.0

WORKDIR /home/

RUN echo "432"

RUN git clone https://github.com/coding-corgi/breadgrow.git

WORKDIR /home/breadgrow/

RUN pip install -r requirements.txt

RUN pip install gunicorn

RUN pip install mysqlclient

EXPOSE 8000

CMD ["bash","-c", "python manage.py collectstatic --noinput --settings=breadgrow.settings.deploy && python manage.py migrate --settings=breadgrow.settings.deploy && gunicorn breadgrow.wsgi  --env DJANGO_SETTINGS_MODULE=breadgrow.settings.deploy --bind 0.0.0.0:8000"]
