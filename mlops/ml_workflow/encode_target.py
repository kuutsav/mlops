from typing import List, Tuple

import numpy as np
from sklearn.preprocessing import LabelEncoder


def get_targetencoder_and_encoded_targets(
    target: List[str],
) -> Tuple[LabelEncoder, np.array]:
    le = LabelEncoder()
    encoded_target = le.fit_transform(target)
    return le, encoded_target
