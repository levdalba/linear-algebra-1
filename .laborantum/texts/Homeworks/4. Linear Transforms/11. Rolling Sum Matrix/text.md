# Rolling Sum Matrix

Write a code that generates a matrix that performs
rolling sum of coordinates of a vector in $N$-dimenional 
space:

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
x_1 \\
x_1 + x_2 \\
\vdots \\
x_1 + x_2 + \dots + x_N
\end{bmatrix}
$$