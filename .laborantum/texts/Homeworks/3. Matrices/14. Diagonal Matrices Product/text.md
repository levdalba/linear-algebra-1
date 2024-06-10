# Diagonal Matrix Product

You are given two square matrices: $A$ and $D$, where $A$ is a 
full matrix and $D$ is a diagonal matrix:

$$
A = \begin{bmatrix}
- & \mathbf a_1 & - \\
& \vdots & \\
- & \mathbf a_N & - \\
\end{bmatrix}
$$

$$
D = \textrm{diag}(d_1, d_2, \dots, d_N) = \begin{bmatrix}
d_1 & & & & \\
& d_2 & & & \\
& & d_3 & & \\
& & & \ddots & \\
& & & & d_N 
\end{bmatrix}
$$

Write a program to calculate the result of $DA$ and $AD$ in 
the fastest possible way.