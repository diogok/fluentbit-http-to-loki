FROM python:3.7-alpine

WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

EXPOSE 8000

ENV PYTHONUNBUFFERED 1
ENV FLASK_APP main.py
ENV PORT 8000

# TODO: run in gunicorn or other proper server
CMD ["flask","run","--host","0.0.0.0"]

COPY main.py /usr/src/app

