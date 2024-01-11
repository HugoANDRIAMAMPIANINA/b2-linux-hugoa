# 1 - Calculatrice

## Build

```
docker build . -t calc
```

## Run

```
# avec un docker run
docker run -e CALC_PORT=<port> -p <port>:<port> -d calc

# avec un docker compose après avoir modifié le port dans le docker-compose.yml
docker compose up -d
```