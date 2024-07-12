import numpy as np

answer = {
    "task1": np.array([[30, 36, 42], [66, 81, 96], [102, 126, 150]]).astype("int64"),
    "task2": np.array([[37, 54], [81, 118]]).astype("int64"),
    "task3": np.array([215, 450]).astype("int64"),
}

A = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 0]])
B = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 0]])
print(np.dot(A, B))
K = np.dot(A, B)
x = np.array([1, 2])
print(np.dot(K, x))
