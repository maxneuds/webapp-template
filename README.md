# Webapp Template
A template for a data-driven webapp with Python fastapi backend and Angular frontend running ETL pipelines on MongoDB.

# Preparation

If no MongoDBs are available, you can create a docker network, the volumes and run the databases on it:
```
docker network create net_mongodb
docker volume create mongodb_data_dev
docker volume create mongodb_data_test
docker volume create mongodb_data_prod
```
