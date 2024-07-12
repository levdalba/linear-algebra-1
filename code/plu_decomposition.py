from gauss_elimination_1 import gauss_elimination_1
import numpy as np


def plu_decomposition(A):
    A = A.astype(float)
    m, n = A.shape
    P = np.eye(m)
    L = np.eye(m)
    U = A.copy()

    for i in range(min(m, n)):
        max_row = np.argmax(np.abs(U[i:m, i])) + i

        if i != max_row:
            U[[i, max_row]] = U[[max_row, i]]
            P[[i, max_row]] = P[[max_row, i]]
            L[[i, max_row], :i] = L[[max_row, i], :i]

        for j in range(i + 1, m):
            if U[j, i] != 0:
                factor = U[j, i] / U[i, i]
                U[j, i:] -= factor * U[i, i:]
                L[j, i] = factor

    return P.T, L, U
