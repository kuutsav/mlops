# MLOps

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Checked with mypy](http://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org/)

A project based example of Data pipelines, ML workflow management, API endpoints
and Monitoring.

Tools used:
- `Data Pipeline`: [Dagster](https://github.com/dagster-io/dagster)
- `ML workflow`: [MLflow](https://github.com/mlflow/mlflow)
- `API Deployment`: [FastAPI](https://github.com/tiangolo/fastapi) 
- `Monitoring`: [ElasticAPM](https://www.elastic.co/apm/)

## Requirements

### Poetry [`Dependency management`]

```bash
$ curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
$ poetry --version
# Poetry version 1.1.10
```

### pre-commit [`Static code analysis`]

```bash
$ pip install pre-commit
$ pre-commit --version
# pre-commit 2.15.0
```

### Minio [`S3 compatible object storage`]

Follow the instructions here - https://min.io/download

## Setup

### Environment setup

```bash
$ poetry install
```

### MLflow

```bash
$ poetry shell
$ export MLFLOW_S3_ENDPOINT_URL=http://127.0.0.1:9000
$ export AWS_ACCESS_KEY_ID=minioadmin
$ export AWS_SECRET_ACCESS_KEY=minioadmin

# make sure that the backend store and artifact locations are same in the .env file as well
$ mlflow server \
    --backend-store-uri sqlite:///mlflow.db \
    --default-artifact-root s3://mlflow \
    --host 0.0.0.0
```

### Minio

```bash
$ export MINIO_ROOT_USER=minioadmin
$ export MINIO_ROOT_PASSWORD=minioadmin

$ mkdir minio_data
$ minio server minio_data --console-address ":9001"

# API: http://192.168.29.103:9000  http://10.119.80.13:9000  http://127.0.0.1:9000
# RootUser: minioadmin
# RootPass: minioadmin

# Console: http://192.168.29.103:9001 http://10.119.80.13:9001 http://127.0.0.1:9001
# RootUser: minioadmin
# RootPass: minioadmin

# Command-line: https://docs.min.io/docs/minio-client-quickstart-guide
#    $ mc alias set myminio http://192.168.29.103:9000 minioadmin minioadmin

# Documentation: https://docs.min.io
```
Go to http://127.0.0.1:9001/buckets/ and create a bucket called `mlflow`.


### Dagster

```bash
$ poetry shell
$ dagit -f mlops/pipeline.py
```

### ElasticAPM

```bash
$ docker-compose -f docker-compose-monitoring.yaml up
```

## TODO
- Setup with `docker-compose`.
- Load testing.
- Test cases.
- CI/CD pipeline.
- Drift detection.
