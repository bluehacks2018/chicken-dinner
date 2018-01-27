FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN mkdir /config/
RUN mkdir /config/requirements
ADD /config/requirements/base.txt /config/requirements/
ADD /config/requirements/production.txt /config/requirements/
ADD /config/requirements/local.txt /config/requirements/
RUN pip install -r /config/requirements/local.txt
RUN mkdir /src;
WORKDIR /src
