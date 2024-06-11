# Sparse Matrix Product

You are given two matrices of the same shape: $A$ and $B$. Matrix $A$ is full
and is given in the form of `numpy.ndarray`.

The second matrix $B$ is **sparse**. That means that the 
majority of the items are equal to $0$ except for $M$. This matrix is given
as a set of non-zero elements of this matrix in form of $3 \times M$ `numpy.ndarray` as row-column-value tuple (COO sparse matrix form):

$$
\begin{bmatrix}
r_1 & c_1 & v_1 \\
r_2 & c_2 & v_2 \\
& \vdots & \\
r_M & c_M & v_M \\
\end{bmatrix}
$$

If in this struct two items correspond to the same location, consider the latter is correct.

Write the most efficient program that calculates $AB$.