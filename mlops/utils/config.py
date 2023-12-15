import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]

INPUT_DATASET_LOC = BASE_DIR.parent / "data/Question_Classification_Dataset.csv"
TEST_SIZE = 0.2


# set environment variables
def set_env_vars():
    with open(BASE_DIR / ".env", "r") as f:
        env_vars = f.readlines()
        env_vars = [
            env_var.strip().split("=") for env_var in env_vars if not env_var.startswith("#") and env_var.strip()
        ]
        for env_key, env_val in env_vars:
            os.environ[env_key] = env_val
