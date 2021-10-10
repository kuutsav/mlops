import re
from typing import List


def preprocess_text(texts: List[str]) -> List[str]:
    return [" ".join(re.findall("\w+", text)).lower() for text in texts]
