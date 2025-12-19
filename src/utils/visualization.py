import matplotlib.pyplot as plt
from typing import List, Optional


def plot_metric(
    values: List[float],
    label: str,
    xlabel: str = "Epochs",
    ylabel: str = "Value",
    title: Optional[str] = None
) -> None:
    """
    Plot a single metric curve.
    """
    plt.plot(range(1, len(values) + 1), values, label=label)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    if title:
        plt.title(title)
    plt.legend()
    plt.grid(True)
    plt.show()


def plot_multiple_metrics(
    metrics: List[List[float]],
    labels: List[str],
    xlabel: str = "Epochs",
    ylabel: str = "Value",
    title: Optional[str] = None
) -> None:
    """
    Plot multiple metric curves on the same graph.
    """
    for values, label in zip(metrics, labels):
        plt.plot(range(1, len(values) + 1), values, label=label)

    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    if title:
        plt.title(title)
    plt.legend()
    plt.grid(True)
    plt.show()
