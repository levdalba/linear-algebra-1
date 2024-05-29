# Exercise

For the following vectors:

$$
\mathbf{a} = \begin{bmatrix}
1 \\
1 \\
1 \\
1
\end{bmatrix}, \quad 
\mathbf{b} = 
\begin{bmatrix}
1 \\
-1 \\
-1 \\
1
\end{bmatrix}, $$

1) Perform the operation $$2 \mathbf a + \mathbf b$$ 
Write the answer as list of coordinates in field `expression`.

2) Calculate $$\left<\mathbf a, \mathbf b\right>$$ 
Write result as a single value in field `dot_prod`

3) Calculate $$|\mathbf a|, |\mathbf b|$$ 
Write results as single values in variables `length_a` and `length_b`.

4) Calculate the angle between $\mathbf a$ and $\mathbf b$ 
    $$\angle(\mathbf a, \mathbf b)$$ 
    in **radians**.
    Write result as a single value in variable `angle`.

5) Find directions of these vectors 
$\mathbf l_{\mathbf{a}}, \mathbf{l}_{\mathbf{b}}$. Write results in form of
lists of coordinates in variables `dir_a` and `dir_b`.

6) Find collinear component (projection) of the vector $\mathbf a$ to
the vector $\mathbf b$ and of $\mathbf b$ to the vector $\mathbf a$. 
Write results in a form of list if 
coordinates in variable `a_proj_b` and `b_proj_a` correspondingly.

7) Find orthogonal component of the vector $\mathbf a$ to
the vector $\mathbf b$ and of the vector $\mathbf b$ to
the vector $\mathbf a$. Write result in a form of list of coordinates
in function `a_orth_b` and `b_orth_a` correspondingly.

This task is for solving by hand.
You are not supposed to use ```numpy``` 
library or any other libraries that can perform vector computations for you.