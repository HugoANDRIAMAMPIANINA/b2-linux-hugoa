FROM debian
RUN apt update
RUN apt install python3 -y
RUN apt install pip -y
RUN apt install python3-emoji
COPY app.py .
ENTRYPOINT ["python3", "app.py"]