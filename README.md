# Webapp Template
A template for a webapp with python Fastapi backend and Angular frontend running data pipelines on MongoDB.

# Preparation

If no MongoDBs are available, you can create a docker network, the volumes and run the databases on it:
```
docker network create net_mongodb
docker volume create mongodb_data_dev
docker volume create mongodb_data_test
docker volume create mongodb_data_prod
```
