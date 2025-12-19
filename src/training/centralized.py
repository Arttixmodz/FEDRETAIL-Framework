import tensorflow as tf
from typing import Tuple


def centralized_training(
    model: tf.keras.Model,
    X_train,
    y_train,
    X_test,
    y_test,
    epochs: int = 200,
    verbose: int = 1
) -> Tuple[list, list]:
    """
    Centralized training baseline.

    Returns
    -------
    accuracy : list
        Validation accuracy per epoch
    loss : list
        Training loss per epoch
    """
    history = model.fit(
        X_train,
        y_train,
        epochs=epochs,
        validation_data=(X_test, y_test),
        verbose=verbose
    )

    return history.history["val_accuracy"], history.history["loss"]
