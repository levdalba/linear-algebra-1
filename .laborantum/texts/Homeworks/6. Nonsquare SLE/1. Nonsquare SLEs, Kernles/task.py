import numpy as np

answer = {
    "task_1": {
        "partial": np.array([[2], [1], [0]]),
        "null_space": None,  # No null space due to inconsistency
    },
    "task_2": {
        "partial": np.array([[6], [8], [0], [0], [0]]),
        "null_space": [
            np.array([[-1], [0], [1], [0], [0]]),
            np.array([[-1], [0], [0], [1], [0]]),
            np.array([[-1], [0], [0], [0], [1]]),
        ],
    },
    "task_3": {
        "partial": np.array([[8], [-6], [0], [0], [0], [0]]),
        "null_space": [
            np.array([[-1], [0], [1], [0], [0], [0]]),
            np.array([[-1], [0], [0], [1], [0], [0]]),
            np.array([[-1], [0], [0], [0], [1], [0]]),
            np.array([[-1], [0], [0], [0], [0], [1]]),
        ],
    },
}
