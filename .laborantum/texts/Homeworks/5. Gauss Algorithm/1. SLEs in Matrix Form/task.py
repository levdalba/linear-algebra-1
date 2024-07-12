import numpy as np

answer = {
    "task_1": {
        "A": np.array([[1, 1], [2, 1]]).astype("int64"),
        "b": np.array([[17, 10]]).T,
        "inv_A": np.array([[-1, 1], [2, -1]]).astype("int64"),
        "L": np.array([[1, 0], [2, -1]]).astype("int64"),
        "U": np.array([[1, 1], [0, 1]]).astype("int64"),
        "x": np.array([[-7, 24]]).T,
    },
    "task_2": {
        "A": np.array([[1, 5], [2, 9]]).astype("int64"),
        "b": np.array([[2, 4]]).T,
        "inv_A": np.array([[-9, 5], [2, -1]]).astype("int64"),
        "L": np.array([[1, 0], [2, -1]]).astype("int64"),
        "U": np.array([[1, 5], [0, 1]]).astype("int64"),
        "x": np.array([[2, 0]]).T,
    },
    "task_3": {
        "A": np.array([[1, 0, 1], [2, 1, -1], [3, 1, -2]]).astype("int64"),
        "b": np.array([[3, 2, 3]]).T,
        "inv_A": np.array(
            [[0.5, -0.5, 0.5], [-0.5, 2.5, -1.5], [0.5, 0.5, -0.5]]
        ).astype("float64"),
        "L": np.array([[1, 0, 0], [0.66666667, 1, 0], [0.33333333, -1, 1]]).astype(
            "float64"
        ),
        "U": np.array([[3, 1, -2], [0, 0.33333333, 0.33333333], [0, 0, 2]]).astype(
            "float64"
        ),
        "x": np.array([[2, -1, 1]]).T.astype("float64"),
    },
    "task_4": {
        "A": np.array([[1, 1, 1, 1], [2, 1, 1, 1], [3, 2, 1, 1], [4, 3, 2, 1]]).astype(
            "int64"
        ),
        "b": np.array([[4, 5, 7, 10]]).T,
        "inv_A": np.array(
            [[-1, 1, 0, 0], [1, -2, 1, -0], [-0, 1, -2, 1], [1, 0, 1, -1]]
        ).astype("float64"),
        "L": np.array(
            [[1, 0, 0, 0], [0.5, 1, 0, 0], [0.75, 0.5, 1, 0], [0.25, -0.5, -1, 1]]
        ).astype("float64"),
        "U": np.array(
            [[4, 3, 2, 1], [0, -0.5, 0, 0.5], [0, 0, -0.5, 0], [0, 0, 0, 1]]
        ).astype("float64"),
        "x": np.array([[1, 1, 1, 1]]).T.astype("float64"),
    },
}
