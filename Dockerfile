FROM python:3.7-alpine
copy . /opt/myapp/
WORKDIR /opt/myapp/
ENTRYPOINT ["python3"]


CMD ["main.py L1.txt L2.txt R.txt"]+
