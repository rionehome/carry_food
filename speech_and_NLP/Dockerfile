FROM python:3.10.9

WORKDIR /app

USER root

RUN apt update -y
RUN apt upgrade -y
RUN apt install cmake ffmpeg mecab libportaudio2 -y

COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .


CMD ["python3", "src/main.py"]