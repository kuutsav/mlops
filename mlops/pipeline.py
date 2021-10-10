from typing import Any, List, Tuple

from dagster import Output, OutputDefinition, pipeline, solid

from mlops.data_processing import dataloaders, featurizer, text_preprocessing
from mlops.ml_workflow import encode_target, naive_bayes_clf, train_test
from mlops.utils.config import INPUT_DATASET_LOC


@solid(
    output_defs=[
        OutputDefinition(name="texts", is_required=True),
        OutputDefinition(name="target", is_required=True),
    ]
)
def get_training_dataset(context):
    texts, target = dataloaders.get_input_dataset(INPUT_DATASET_LOC)
    context.log.info(f"Loaded data; N={len(texts)}, Targets={set(target)}")
    yield Output(texts, "texts")
    yield Output(target, "target")


@solid
def preprocess_text(context, texts):
    texts = text_preprocessing.preprocess_text(texts)
    context.log.info(f"Text pre-processing done; N={len(texts)}")
    return texts


@solid(
    output_defs=[
        OutputDefinition(name="vectorizer", is_required=True),
        OutputDefinition(name="X", is_required=True),
    ]
)
def get_vectorizer_and_features(context, texts):
    vectorizer, X = featurizer.get_vectorizer_and_features(texts)
    context.log.info(f"Featurized text; Shape={X.shape}")
    yield Output(vectorizer, "vectorizer")
    yield Output(X, "X")


@solid(
    output_defs=[
        OutputDefinition(name="target_encoder", is_required=True),
        OutputDefinition(name="encoded_target", is_required=True),
    ]
)
def get_targetencoder_and_encoded_targets(context, target):
    (
        target_encoder,
        encoded_target,
    ) = encode_target.get_targetencoder_and_encoded_targets(target)
    context.log.info(
        f"Target encoded; Shape={len(encoded_target)}, Classes={target_encoder.classes_}"
    )
    yield Output(target_encoder, "target_encoder")
    yield Output(encoded_target, "encoded_target")


@solid(
    output_defs=[
        OutputDefinition(name="X_train", is_required=True),
        OutputDefinition(name="X_test", is_required=True),
        OutputDefinition(name="y_train", is_required=True),
        OutputDefinition(name="y_test", is_required=True),
    ]
)
def train_test_split(context, texts, target):
    X_train, X_test, y_train, y_test = train_test.get_train_test_split(texts, target)
    context.log.info(
        f"Train test split done; X_train={X_train.shape}, X_test={X_test.shape}, "
        f"y_train={y_train.shape}, y_test={y_test.shape}"
    )
    yield Output(X_train, "X_train")
    yield Output(X_test, "X_test")
    yield Output(y_train, "y_train")
    yield Output(y_test, "y_test")


@solid
def train_clf(context, X_train, X_test, y_train, y_test) -> None:
    report = naive_bayes_clf.train_and_validate_clf(X_train, X_test, y_train, y_test)
    context.log.info(report)


@pipeline
def ml_pipeline():
    texts, target = get_training_dataset()
    vectorizer, X = get_vectorizer_and_features(preprocess_text(texts))
    target_encoder, encoded_target = get_targetencoder_and_encoded_targets(target)
    X_train, X_test, y_train, y_test = train_test_split(X, encoded_target)
    train_clf(X_train, X_test, y_train, y_test)
