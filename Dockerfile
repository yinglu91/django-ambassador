FROM python:3.9
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
COPY . /app

CMD python manage.py wait_for_db && python manage.py runserver 0.0.0.0:8000


# "python manage.py makemigrations && 
#               python manage.py migrate && 
#               python manage.py runserver 0.0.0.0:8000"
# docker run -itd --name db -p 3306:3306 -e MYSQL_ROOT_PASSWORD=root mysql

# One liner to stop / remove all of Docker containers:

# docker stop $(docker ps -a -q)
# docker rm $(docker ps -a -q)

# $ docker-compose up

# https://github.com/antoniopapa/django-ambassador/blob/main/docker-compose.yaml
