FROM python:3.8.0-slim

RUN mkdir /docker_test
WORKDIR /docker_test
COPY requirement.txt /docker_test/
RUN pip install -r requirement.txt
COPY . /docker_test/

CMD python3 manage.py makemigrations
CMD python3 manage.py migrate
CMD python3 manage.py runserver 0.0.0.0:8000
