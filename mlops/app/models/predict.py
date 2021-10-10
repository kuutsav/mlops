from typing import Dict

from pydantic import BaseModel


class PredictResponseModel(BaseModel):
    preds: Dict[str, float]
