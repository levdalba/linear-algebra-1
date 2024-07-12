from gauss_elimination_1 import gauss_elimination_1
import numpy as np


def find_kernel(A):
    A_reduced, pivot_columns = gauss_elimination_1(A)

    n = A.shape[1]
    non_pivot_columns = [j for j in range(n) if j not in pivot_columns]

    identity_matrix = np.eye(len(non_pivot_columns))

    null_space_basis = []
    for i, col in enumerate(non_pivot_columns):
        vector = np.zeros(n)
        vector[non_pivot_columns] = -identity_matrix[:, i]
        vector[col] = 1
        null_space_basis.append(vector)

    if not null_space_basis:
        return np.zeros((n, 1))

    B = np.column_stack(null_space_basis)

    return B
