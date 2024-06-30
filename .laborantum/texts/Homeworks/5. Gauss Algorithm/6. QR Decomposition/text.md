# QR decomposition

You are given a column-matrix $A$. Perform QR composition (write a function that 
finds two matrices $Q$ and $R$ such that $Q$ is an orthogonal matrix $Q^T Q = I$ 
and $R$ is an upper-triangular matrix.

## Hints

This process is rather simple:

1)  Perform orthonormalization procedure for the columns of the matrix, from
    left to right. Add only non-zero vectors to the resulting system strictly
    in the order of appearance

2)  Find decomposition of each of the column vectors through the abovementioned
    system of orthonormal vectors

3)  A vector $\mathbf a$ can be written out as:

    $$\mathbf a = \begin{bmatrix}
    | & | & & | \\
    \mathbf q_1 & \mathbf q_2 & \dots & \mathbf q_n \\
    | & | & & | \\ 
    \end{bmatrix}
    \begin{bmatrix}
    \left< \mathbf a, \mathbf q_n\right> \\
    \vdots \\
    \left< \mathbf a, \mathbf q_n\right>
    \end{bmatrix}$$

4)  If you consider a vector $\mathbf a_k$, then it can either be linearly
    independent on the previous vectors 
    $$ \left\{\mathbf a_1, \dots, \mathbf a_{k-1}\right\},$$
    or linearly dependent.
    In any case, it can be represented as 
    $$\mathbf a_k = \sum_{l=1}^k \alpha_k \mathbf q_l,$$
    which takes into account only the components that appeared not later than 
    $\mathbf q_k$.

5)  Hence, the right side matrix can only be upper-triangular, and hence,
    any matrix $A$ can be decomposed into product of matrices $Q$ and $R$, where
    $Q$ matrix holds an orthonormal set of vectors, and the matrix $R$ holds
    the coordinates of the vectors from $A$ in orthonormal basis $Q$.