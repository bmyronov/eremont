FROM python:3.11.4

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# update system
RUN apt update && \
    apt upgrade -y && \
    apt install -y --no-install-recommends gcc

# set work directory
WORKDIR /web

# copy project files into working directory
COPY . .

# create static and media directories
RUN mkdir /web/static
# RUN mkdir /web/media # if not created

# update pip 
RUN pip install --upgrade pip

# install poetry
RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev

CMD ["gunicorn","-b","0.0.0.0:5000","eremont.wsgi:application"]