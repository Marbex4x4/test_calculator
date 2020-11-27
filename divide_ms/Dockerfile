FROM python:3.8.3-slim-buster
ENV LANG C.UTF-8

WORKDIR /app  
COPY . .

RUN apt-get update \
    && yes | apt-get install bash \
    && chmod +x entrypoint.sh \
    && pip3 install -r requirements.txt \
    && ls -la

EXPOSE 8080

ENTRYPOINT ["./entrypoint.sh"]