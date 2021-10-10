import csv
from typing import List, Tuple


def get_input_dataset(csv_path: str) -> Tuple[List[str], List[str]]:
    with open(csv_path, "r") as f:
        data = [row for row in csv.reader(f)][1:]
        texts, target = [d[0] for d in data], [d[1] for d in data]
        return texts, target
