# pull official base image
FROM python:3.8.8

# set work directory
WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DEBUG 0


# install dependencies
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . .


# run gunicorn
CMD gunicorn hello_django.wsgi:application --bind 0.0.0.0:$PORT