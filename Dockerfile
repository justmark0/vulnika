FROM python:3.9
RUN apt update && apt install -yq socat curl wget netcat
WORKDIR /app
ADD app/requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
ADD app .
ENTRYPOINT ["python3", "/app/main.py"]