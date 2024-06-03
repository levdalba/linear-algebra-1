# 3-dimensional arrays

It is time to start working with 3 dimensional arrays. That
might be useful when you want to speed up some calculations.

## Task

You are given a set of $N$ basis vectors in the form of row-matrix $B$ of size $N \times M$ and a set of **contravariant** coordinates in that basis $C$ for $K$ vectors of size $N \times K$:

$$B = 
\begin{bmatrix}
- & \mathbf b_1 & - \\
- & \mathbf b_2 & - \\
  & \dots & \\
- & \mathbf b_N & -
\end{bmatrix}$$

$$C =
\begin{bmatrix}
c_1^1 & c_1^2 & \dots & c_1^K \\
c_2^1 & c_2^2 & \dots & c_2^K \\
\vdots & \vdots & \ddots & \vdots \\
c_N^1 & c_N^2 & \dots & c_N^K \\
\end{bmatrix}
$$

Thus, $N$ is the number of the basis
vectors and, thus number of coordinates in the span,
$M$ is the dimensionality of the space, $K$ is the number of vectors to reconstruct.

**The task is** to reconstruct the vectors that are defined using these coordinates. The answer should be
a matrix of shape $K \times M$

**You should not use the cycles in this task**

# Interface

## Inputs

`B, C` -- 2D `numpy` arrays

## Outputs

`V` -- 2D `numpy` array


<details>
<summary> <b>Hint</b> </summary>
So, how are you supposed to deal with this task?

If you are allowed to use cycles, that is rather simple: you
iterate over the basis vectors and corresponding coordinates,
multiply one with another and collect the result one-by-one.

But the trick here is that you should do that in a vectorized
manner. So, how to deal with it?

We want in the end to recieve an array of the size 
$K \times M$.

And here is how this get it:
1) reshape your basis vectors to the size of 
$N \times 1 \times M$. It is non-trivial to do that with
usual `reshape`, so there is a function 
`numpy.expand_dims(x, position)` that allows to add a
dimension of an array to the specified position. In this
case the `position=1` as we want to insert dimension of
size `1` to the first position.
2) reshape the coordinates in this basis to the size of
$N \times K \times 1$. Use `numpy.expand_dims` yet again.
3) multiply two tensors from above and receive array of size
$N \times K \times M$. This will first cast the shapes of 
the abovementioned arrays and then perform the multiplication.
This result holds all the required products you may ever need.
4) Now sum this array along the `axis=0` to get $K \times M$
array.
5) Enjoy

Note that although this approach works really fast, it
requires quite a lot of memory. There is another way of doing
this operation that we will study later.
</details>