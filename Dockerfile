# pull official base image
FROM python:3-alpine

ENV NAME=hogon
ENV HOME=/hogon
LABEL Name="Hogon" Version="0.1.0"


# set work directory
RUN mkdir $HOME
RUN mkdir $HOME/statics
WORKDIR $HOME

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt --no-cache-dir

# copy project
COPY . .

# create the $NAME user
RUN addgroup -S $NAME && adduser -S $NAME -G $NAME

# chown all the files to the $NAME user
RUN chown -R $NAME:$NAME $HOME

# change to the $NAME user
USER $NAME