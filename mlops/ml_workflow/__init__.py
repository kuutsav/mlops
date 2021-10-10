import os

from mlops.utils.config import BASE_DIR


# set environment variables
with open(BASE_DIR / ".env", "r") as f:
    env_vars = f.readlines()
    env_vars = [
        env_var.strip().split("=")
        for env_var in env_vars
        if not env_var.startswith("#") and env_var.strip()
    ]
    for env_key, env_val in env_vars:
        os.environ[env_key] = env_val
