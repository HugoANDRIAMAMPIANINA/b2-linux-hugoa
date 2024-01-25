# 2 - Chatroom

## Build

```
docker build . -t chatroom
```

## Run

```
# avec un docker run
docker run -e CHAT_PORT=<port> -p <port>:<port> -d chatroom

# avec un docker compose après avoir modifié le port dans le docker-compose.yml
docker compose up -d
```