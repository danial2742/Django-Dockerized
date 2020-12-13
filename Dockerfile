# pull official base image
FROM python:3.9-alpine

ENV NAME=app
ENV HOME=/app

# set work directory
RUN mkdir $HOME
RUN mkdir $HOME/statics
RUN mkdir $HOME/medias
WORKDIR $HOME

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# copy project
COPY . .

# install psycopg2 dependencies
RUN apk add --no-cache --virtual .build-deps \
    ca-certificates gcc postgresql-dev linux-headers musl-dev \
    libffi-dev jpeg-dev zlib-dev \
    && pip install -r requirements.txt \
    && find /usr/local \
        \( -type d -a -name test -o -name tests \) \
        -o \( -type f -a -name '*.pyc' -o -name '*.pyo' \) \
        -exec rm -rf '{}' + \
    && runDeps="$( \
        scanelf --needed --nobanner --recursive /usr/local \
                | awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \
                | sort -u \
                | xargs -r apk info --installed \
                | sort -u \
    )" \
    && apk add --virtual .rundeps $runDeps \
    && apk del .build-deps

# create the $NAME user
RUN addgroup -S $NAME && adduser -S $NAME -G $NAME

# chown all the files to the $NAME user
RUN chown -R $NAME:$NAME $HOME

# change to the $NAME user
#USER $NAME