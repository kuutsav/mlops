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
