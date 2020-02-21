FROM python:3
RUN apt-get update
RUN apt install -y python3-pip
COPY requirements.txt /opt/
WORKDIR /opt/
RUN pip3 install -r requirements.txt
ADD . /opt
CMD [ "python3", "./main.py" ]
