FROM python:3.11.9-alpine
WORKDIR /usr/src/app
COPY . .
RUN python setup.py install
ENTRYPOINT [ "wafw00f" ]
