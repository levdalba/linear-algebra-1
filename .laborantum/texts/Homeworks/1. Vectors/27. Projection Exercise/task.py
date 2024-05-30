import numpy as np

answer = {
    'proj_a_b': [0.5, 0.5, 1.5, 1.5, 2.],
    'orth_a_b': [ 5.5,  2.5,  0.5, -0.5, -2.],
    'proj_b_a': [2.16, 1.08, 0.72, 0.36, 0.],
    'orth_b_a': [-1.16, -0.08, 2.28,  2.64,  4.]
}

# a = np.array([6,3,2,1,0])
# b = np.array([1,1,3,3,4])

# proj_a_b = np.dot(a,b)/np.dot(b,b)*b
# orth_a_b = a - proj_a_b
# proj_b_a = np.dot(a,b)/ np.dot(a,a)*a
# orth_b_a = b - proj_b_a

# print(proj_a_b)
# print(orth_a_b)
# print(proj_b_a)
# print(orth_b_a)