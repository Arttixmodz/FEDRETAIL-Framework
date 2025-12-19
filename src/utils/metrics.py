from typing import List, Dict


def extract_accuracy(history: Dict) -> List[float]:
    """
    Extract accuracy from a Keras History object dictionary.
    """
    return history.get("accuracy", [])


def extract_val_accuracy(history: Dict) -> List[float]:
    """
    Extract validation accuracy from a Keras History object dictionary.
    """
    return history.get("val_accuracy", [])


def extract_loss(history: Dict) -> List[float]:
    """
    Extract training loss from a Keras History object dictionary.
    """
    return history.get("loss", [])


def extract_val_loss(history: Dict) -> List[float]:
    """
    Extract validation loss from a Keras History object dictionary.
    """
    return history.get("val_loss", [])
