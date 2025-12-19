import tensorflow as tf
from tensorflow.keras import layers, models


def create_neural_network(
    input_shape=(28, 28),
    num_classes=10,
    learning_rate=0.001
) -> tf.keras.Model:
    """
    Creates a Neural Network model used in FEDRETAIL
    for centralized and horizontal federated learning.

    Parameters
    ----------
    input_shape : tuple
        Shape of input images (default: Fashion-MNIST 28x28)
    num_classes : int
        Number of output classes
    learning_rate : float
        Learning rate for Adam optimizer

    Returns
    -------
    tf.keras.Model
        Compiled Keras model
    """
    model = models.Sequential([
        layers.Flatten(input_shape=input_shape),
        layers.Dense(128, activation="relu"),
        layers.Dropout(0.2),
        layers.Dense(num_classes, activation="softmax")
    ])

    model.compile(
        optimizer=tf.keras.optimizers.Adam(learning_rate=learning_rate),
        loss="sparse_categorical_crossentropy",
        metrics=["accuracy"]
    )

    return model
