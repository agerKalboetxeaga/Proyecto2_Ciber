# Base
FROM python:3.8

# setup env var
ENV DockerHOME=/home/app/webapp

# work dir
RUN mkdir -p $DockerHOME

WORKDIR $DockerHOME

# install things
RUN pip install --upgrade pip

# Copy django project
COPY . $DockerHOME

#Install requirements.txt
RUN pip install -r requirements.txt

# Port for Django
EXPOSE 8000

# start server
CMD python manage.py runserver