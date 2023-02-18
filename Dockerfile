FROM python:bullseye

COPY . /

RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    python3-dev \
    python3-pip \
    python3-setuptools \
    python3-wheel \
    python3-venv \
    && rm -rf /var/lib/apt/lists/*
RUN pip3 install --upgrade pip
RUN pip install pandas
RUN pip install flask
RUN pip install flask_sqlalchemy
RUN pip install flask_migrate
RUN pip install requests
RUN pip install flask_wtf
RUN pip install gunicorn
RUN useradd mike

EXPOSE 8000
USER mike
CMD gunicorn -w 1 "app:create_app()" 