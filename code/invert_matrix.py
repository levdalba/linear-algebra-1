from gauss_elimination_1 import gauss_elimination_1
from gauss_elimination_2 import gauss_elimination_2
import numpy as np


def invert_matrix(A):
    if A.shape[0] != A.shape[1]:
        return None

    augmented_matrix = np.hstack((A, np.eye(A.shape[0])))
    augmented_matrix = gauss_elimination_1(augmented_matrix)

    augmented_matrix = gauss_elimination_2(augmented_matrix)
    if not np.allclose(augmented_matrix[:, : A.shape[0]], np.eye(A.shape[0])):
        return None  
    return augmented_matrix[:, A.shape[0] :]
