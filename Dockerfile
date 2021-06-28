FROM python:3.9

WORKDIR /app

COPY requirements.txt /app

RUN pip install -r requirements.txt --no-cache-dir

COPY . .

CMD gunicorn --bind 0.0.0.0:5000 app:app
