FROM python:3.7-alpine
WORKDIR /usr/src/app
COPY ./requirements.txt /usr/src/app

RUN  pip install --no-cache-dir -r requirements.txt

COPY ./topic-creator.py /usr/src/app
COPY ./Producer.py /usr/src/app
CMD [ "python", "./topic-creator.py" ]
CMD [ "python", "./Producer.py" ]