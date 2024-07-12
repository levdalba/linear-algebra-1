import numpy as np


def gauss_elimination_1(A, B, permutations=True):
    A = A.astype(float)
    B = B.astype(float)
    P = np.eye(A.shape[0])

    n = A.shape[0]

    for k in range(n):
        if permutations:
            max_row_index = np.argmax(np.abs(A[k:, k])) + k
            if max_row_index != k:
                A[[k, max_row_index]] = A[[max_row_index, k]]
                B[[k, max_row_index]] = B[[max_row_index, k]]
                P[[k, max_row_index]] = P[[max_row_index, k]]

        if A[k, k] == 0:
            continue

        for i in range(k + 1, n):
            factor = A[i, k] / A[k, k]
            A[i, k:] -= factor * A[k, k:]
            B[i] -= factor * B[k]

        diag_factor = A[k, k]
        if diag_factor != 0:
            A[k] /= diag_factor
            B[k] /= diag_factor

    return P, A, B


