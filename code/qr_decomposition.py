import numpy as np


def qr_decomposition(A):
    A = A.astype(float)
    n, m = A.shape
    Q = np.zeros((n, m))
    R = np.zeros((m, m))

    for j in range(m):
        v = A[:, j]
        for i in range(j):
            R[i, j] = np.dot(Q[:, i], A[:, j])
            v = v - (R[i, j] * Q[:, i])
        R[j, j] = np.linalg.norm(v)
        if R[j, j] != 0:
            Q[:, j] = v / R[j, j]

    return Q, R
