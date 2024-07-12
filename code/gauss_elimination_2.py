import numpy as np


def gauss_elimination_2(A, B):
    A = A.astype(float)
    B = B.astype(float)
    n = A.shape[0]

    for i in range(n - 1, 0, -1):
        for j in range(i - 1, -1, -1):
            factor = A[j, i] / A[i, i]
            A[j, :] -= factor * A[i, :]
            B[j, :] -= factor * B[i, :]

    return A, B
