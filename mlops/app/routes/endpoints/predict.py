import pickle

import mlflow.sklearn
from fastapi import APIRouter
from loguru import logger

from mlops.app.models.predict import PredictResponseModel
from mlops.data_processing.text_preprocessing import preprocess_text
from mlops.utils.config import BASE_DIR, set_env_vars

# setting env vars here for mlflow configuration
set_env_vars()
router = APIRouter()

# manually pick the model version from trained models
sk_model = mlflow.sklearn.load_model(model_uri="models:/sk-learn-naive-bayes-clf-model/1")

# mlflow does not store data manipulation routines like label encoding
# we need to manage the LabelEncoder and TfidfVectorizer ourselves
with open(BASE_DIR / "artifacts/target_encoder.pkl", "rb") as f:
    target_encoder = pickle.load(f)
with open(BASE_DIR / "artifacts/vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)
logger.info("Loaded model artifacts")


@router.post("/predict")
async def predit(text: str) -> PredictResponseModel:
    logger.info(f"Received text for prediction: {text}")
    processed_text_list = preprocess_text([text])
    x = vectorizer.transform(processed_text_list)
    pred = sk_model.predict_proba(x)
    mapped_pred = dict(zip(target_encoder.classes_, pred[0]))
    logger.info(f"Prediction: {mapped_pred}")

    return PredictResponseModel(preds=mapped_pred).preds
