# run

First, make sure to create the correct networks and volumes:

```
docker network create net_mongodb
docker volume create mongodb_data_dev
docker volume create mongodb_data_test
docker volume create mongodb_data_prod
```

Next, copy `config.example.env` to `config.env` and edit it according to your needs.
Finally, start and stop the containers using Docker Compose:

```
docker compose --env-file config.env up -d
docker compose --env-file config.env down
```
