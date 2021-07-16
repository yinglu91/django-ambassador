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
# $ docker-compose up --build   #re-build then run

# https://github.com/antoniopapa/django-ambassador/blob/main/docker-compose.yaml


############ to check redis cache keys
# $ docker container ls -a |grep redis

# $ docker exec --user root -it 7ccd99bbf8a7 sh
# # redis-cli
# 127.0.0.1:6379> KEYS *
# 1) ":1:views.decorators.cache.cache_header.products_frontend.dc90228079ec44a3766ce12605301f6a.en-us.UTC"
# 2) ":1:products_backend"
# 3) ":1:views.decorators.cache.cache_page.products_frontend.GET.dc90228079ec44a3766ce12605301f6a.65330eb47d0175f264fdb29633829c0b.en-us.UTC"
# 127.0.0.1:6379>
# AFTER UPDATE products  PUT http://localhost:8000/api/admin/products/2
# 127.0.0.1:6379> KEYS *
# (empty list or set)
# 127.0.0.1:6379>
############ end check redis cache keys