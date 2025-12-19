import numpy as np
from typing import List, Tuple


def non_iid_split(
    X: np.ndarray,
    y: np.ndarray,
    num_clients: int,
    shards_per_client: int = 2,
    shuffle: bool = True,
    seed: int | None = None
) -> Tuple[List[np.ndarray], List[np.ndarray]]:
    """
    Non-IID data split using label-based shards.

    Parameters
    ----------
    X : np.ndarray
        Input features
    y : np.ndarray
        Labels
    num_clients : int
        Number of clients
    shards_per_client : int
        Number of label shards per client
    shuffle : bool
        Shuffle shards before assignment
    seed : int | None
        Random seed

    Returns
    -------
    clients_X : List[np.ndarray]
        Feature splits per client
    clients_y : List[np.ndarray]
        Label splits per client
    """
    if num_clients <= 0 or shards_per_client <= 0:
        raise ValueError("num_clients and shards_per_client must be > 0")

    if len(X) != len(y):
        raise ValueError("X and y must have the same length")

    if seed is not None:
        np.random.seed(seed)

    # Sort data by labels
    sorted_indices = np.argsort(y)
    X_sorted = X[sorted_indices]
    y_sorted = y[sorted_indices]

    num_shards = num_clients * shards_per_client
    shard_size = len(X_sorted) // num_shards

    if shard_size == 0:
        raise ValueError("Dataset too small for the number of shards")

    shards_X = [
        X_sorted[i * shard_size:(i + 1) * shard_size]
        for i in range(num_shards)
    ]
    shards_y = [
        y_sorted[i * shard_size:(i + 1) * shard_size]
        for i in range(num_shards)
    ]

    shard_indices = np.arange(num_shards)
    if shuffle:
        np.random.shuffle(shard_indices)

    clients_X, clients_y = [], []
    for i in range(num_clients):
        assigned = shard_indices[
            i * shards_per_client:(i + 1) * shards_per_client
        ]
        clients_X.append(np.concatenate([shards_X[j] for j in assigned]))
        clients_y.append(np.concatenate([shards_y[j] for j in assigned]))

    return clients_X, clients_y
