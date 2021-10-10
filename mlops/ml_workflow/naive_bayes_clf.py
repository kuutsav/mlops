import mlflow
import mlflow.sklearn
import numpy as np
from sklearn.metrics import classification_report, precision_recall_fscore_support
from sklearn.naive_bayes import MultinomialNB

mlflow.set_tracking_uri("http://localhost:5000")


def train_and_validate_clf(
    X_train: np.array, X_test: np.array, y_train: np.array, y_test: np.array
) -> str:
    with mlflow.start_run(run_name="NAIVE_BAYES_CLF"):
        clf = MultinomialNB()
        mlflow.log_param("alpha", clf.get_params()["alpha"])
        clf.fit(X_train, y_train)
        y_pred = clf.predict(X_test)
        scores = precision_recall_fscore_support(y_test, y_pred, average="weighted")
        mlflow.log_metric("precision", scores[0])
        mlflow.log_metric("recall", scores[1])
        mlflow.log_metric("f1_score", scores[2])
        mlflow.sklearn.log_model(
            sk_model=clf,
            artifact_path="sklearn-model",
            registered_model_name="sk-learn-naive-bayes-clf-model",
        )

        return classification_report(y_test, y_pred)
