import numpy as np


def find_solution(A, b):
    A = A.astype(float)
    b = b.astype(float)

    n = len(A)
    for i in range(n):
        for j in range(i + 1, n):
            if abs(A[j][i]) > abs(A[i][i]):
                A[[i, j]] = A[[j, i]]
                b[[i, j]] = b[[j, i]]
        for j in range(i + 1, n):
            ratio = A[j][i] / A[i][i]
            for k in range(i, n):
                A[j][k] -= ratio * A[i][k]
            b[j] -= ratio * b[i]

    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = b[i]
        for j in range(i + 1, n):
            x[i] -= A[i][j] * x[j]
        x[i] = x[i] / A[i][i]
    return x
