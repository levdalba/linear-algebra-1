# Task

You want to define an $(N-1)$-dimensional hyperplane 
in $N$-dimensional space using the following expression:
$$\left\{ \forall \mathbf x: \left<\mathbf x, \mathbf a\right> + b = 0\right\},$$

where $\mathbf a$ and $b$ are the parameters that you can control.

You want the hyperplane to include the point $\mathbf x_0$. 
You have to write the function `bias` that calculates
the necessary parameter `b` for that to happen.

## Interface

Inputs: ```a: numpy.ndarray, x0: numpy.ndarray```

Outputs: ```b: float```