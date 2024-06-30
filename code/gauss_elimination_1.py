import numpy as np

def gauss_elimination_1(A, B, permutations=True):
    A = A.astype(float)
    B = B.astype(float)
    P = np.eye(A.shape[0])
    
    ## YOUR CODE HERE

    return P, A, B

