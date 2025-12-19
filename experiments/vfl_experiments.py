import tensorflow as tf
from tensorflow.keras.datasets import fashion_mnist

from src.models import create_logistic_regression
from src.data import iid_split
from src.training import vertical_federated_training
from src.utils.visualization import plot_metric


def run_vfl_experiments():
    (X_train, y_train), (X_test, y_test) = fashion_mnist.load_data()

    num_clients = 5
    rounds = 50

    clients_X, clients_y = iid_split(X_train, y_train, num_clients)

    model = create_logistic_regression()

    accuracy, _ = vertical_federated_training(
        global_model=model,
        clients_X=clients_X,
        clients_y=clients_y,
        X_test=X_test,
        y_test=y_test,
        rounds=rounds,
        local_epochs=2
    )

    plot_metric(
        values=accuracy,
        label="VFL Accuracy",
        ylabel="Accuracy",
        title="Vertical Federated Learning Performance"
    )


if __name__ == "__main__":
    run_vfl_experiments()
