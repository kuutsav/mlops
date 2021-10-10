from typing import List, Tuple

import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer


def get_vectorizer_and_features(texts: List[str]) -> Tuple[TfidfVectorizer, np.array]:
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(texts)
    return vectorizer, X
