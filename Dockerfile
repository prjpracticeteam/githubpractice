FROM python:3.7-alpine
COPY . /opt/app/
WORKDIR /opt/app/
CMD [ "main.py" ]
