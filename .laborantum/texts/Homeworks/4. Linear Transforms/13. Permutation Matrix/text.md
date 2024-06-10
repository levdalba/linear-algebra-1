# Permutation Matrix

You are given a permutation $\sigma$ (order, the permuted 
elements should go in).

Write a program that generates a matrix that permutes
coordinates in vector:

$$
\begin{bmatrix}
x_1 \\
x_2 \\
\vdots \\
x_N
\end{bmatrix}
\rightarrow
A
\rightarrow
\begin{bmatrix}
x_{\sigma_1} \\
x_{\sigma_2} \\
\vdots \\
x_{\sigma_N}
\end{bmatrix}
$$

For example, if you are given a permutation $\sigma = (3, 4, 2, 1)$,
the resulting vector should have the following form:

$$[x_3, x_4, x_2, x_1]^T$$