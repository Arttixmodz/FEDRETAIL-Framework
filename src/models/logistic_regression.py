import tensorflow as tf
from tensorflow.keras import layers, models, optimizers


def create_logistic_regression(
    input_shape=(28, 28),
    num_classes=10,
    learning_rate=0.001
) -> tf.keras.Model:
    """
    Creates a Logistic Regression model for
    Vertical Federated Learning (VFL) in FEDRETAIL.

    Parameters
    ----------
    input_shape : tuple
        Shape of input images
    num_classes : int
        Number of output classes
    learning_rate : float
        Learning rate for optimizer

    Returns
    -------
    tf.keras.Model
        Compiled Keras model
    """
    model = models.Sequential([
        layers.Flatten(input_shape=input_shape),
        layers.Dense(num_classes, activation="softmax")
    ])

    optimizer = optimizers.Adam(learning_rate=learning_rate)

    model.compile(
        optimizer=optimizer,
        loss="sparse_categorical_crossentropy",
        metrics=["accuracy"]
    )

    return model
