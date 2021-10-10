# MLOps

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Checked with mypy](http://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org/)

A project based example of data pipelines, ML workflow management, deployment
and monitoring.

## Requirements

### Poetry

```bash
$ curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
$ poetry --version
# Poetry version 1.1.10
```

### pre-commit

```bash
$ pip install pre-commit
$ pre-commit --version
# pre-commit 2.15.0
```

### Minio

```bash
$ export MINIO_ROOT_USER=minioadmin
$ export MINIO_ROOT_PASSWORD=minioadmin

$ minio server /mnt/data
```

## Setup

```bash
$ poetry install
```

```bash
$ export MLFLOW_S3_ENDPOINT_URL=http://127.0.0.1:9000
$ export AWS_ACCESS_KEY_ID=minioadmin
$ export AWS_SECRET_ACCESS_KEY=minioadmin
```

```bash
$ mlflow server \                                   
    --backend-store-uri sqlite:///mlflow.db \
    --default-artifact-root s3://mlflow \
    --host 0.0.0.0
```
