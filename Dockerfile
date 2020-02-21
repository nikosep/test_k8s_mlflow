FROM python:3
RUN apt install python3-pip
COPY . /opt/app
WORKDIR /opt/app
RUN pip3 install -r requirements.txt
