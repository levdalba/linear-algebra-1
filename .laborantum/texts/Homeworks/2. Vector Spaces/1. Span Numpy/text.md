# Numpy 2D arrays

One can store several `numpy` vectors in 2D array in one
of two possible ways. First one is called a **row-matrix**,
where the vectors are listed as rows one by one:

$$
\begin{bmatrix}
- & \mathbf a_1 & - \\
- & \mathbf a_2 & - \\
  & \dots       &   \\
- & \mathbf a_N & - 
\end{bmatrix}
$$

Alternative is called the **column-matrix**, where the
vectors are stored in columns:


$$
\begin{bmatrix}
| & | & & | \\
\mathbf a_1 & \mathbf a_2 & \dots & \mathbf a_N \\
| & | & & |
\end{bmatrix}
$$

To create these matrices usually one calls 
`numpy.hstack`
or `numpy.vstack` functions with list of vectors.

Suppose that you have a matrix `A` (i.e, the table with 
numbers of size $N \times M$) and you want to access an 
element in the row $i$ and column $j$. You can do so
using the indexing operator: `A[i, j]`.

To select the whole `i`-th row, you may use ellipsis: 
`A[i, :]`. The same can be done using the ordinary
indexing as first the indexing happen with rows: `A[i]`.

To select the whole `j`-th column, you may do so:
`A[:, j]`.

## Task

You are given one 2D `numpy.ndarray` that stores 
**column-matrix** `A` with vectors and 1D `numpy.ndarray`
`b` that stores coefficients for these vectors.

Compute the vector that is the linear combination of
the vectors in `A` that are weighted with coefficients
in `b`.

## Shape casting

To solve this task using vectorised operations, you
should multiply every column (i.e., all the elements
in a column) with corresponding 
coefficient and then sum all the columns. 
That is possible to do elementwise 
multiplication of two matrices, one of which contains
in all the same values in all positions in one column:

$$
\begin{bmatrix}
| & | & & | \\
\mathbf a_1 & \mathbf a_2 & \dots & \mathbf a_N \\
| & | & & |
\end{bmatrix} \cdot
\begin{bmatrix}
b_1 & b_2 & \dots & b_N \\
b_1 & b_2 & \dots & b_N \\
\vdots & \vdots & \ddots & \vdots \\
b_1 & b_2 & \dots & b_N
\end{bmatrix}
$$

To create such matrix from a vector is not hard using 
`numpy`. But numpy allows to simplify this procedure
even more. 

If you perform the following operation

$$
\begin{bmatrix}
| & | & & | \\
\mathbf a_1 & \mathbf a_2 & \dots & \mathbf a_N \\
| & | & & |
\end{bmatrix} \cdot
\begin{bmatrix}
b_1 & b_2 & \dots & b_N 
\end{bmatrix},
$$

`numpy` will try to cast all the dimensions of the
matrix (i.e., width and height) to the size
that is required to perform the operation.

Sometimes if amount of diemnsions is different,
it even tries to guess, which dimension should be
casted. But very often this feature causes
lots of troubles. It is easy to avoid these issues by
performing operations only with arrays with the same
number of dimensions.

This being said, you should perform elementwise 
operations only either with two 1D arrays or with
two 2D arrays, or with two N-D arrays.

We have worked with vectors as with 1D arrays before.
To turn 1D array `x` to 2D array, you should do one
of two approaches:

1) `x.reshape([-1, 1])` will turn a vector to a column
vector
2) `x.reshape([1, -1])` will turn a vector to a row 
vector

`-1` in reshapes indicates that `numpy` should 
automatically detect amount of items in that direction
so that all the elements in the original array fit into
the new one. In case that is not possible, `reshape`
operation will raise an exception.

## Summation along the axis

You can perform summation using `x.sum` operation
not only of all the elements in the array (which is
the default behaviour), but also you can sum the array
only along one of the axes. The axis that you want to
sum through is specified in `axis=` parameter. `axis=0`
means that the array will be summed along the columns
resulting in one row, `axis=1` means that the result will
be one column. One should note that dimension
along which the summation is performed is dropped 
by default.

## Interface

```
def linear_combination(
        A: npt.NDArray[np.number], 
        b: npt.NDArray[np.number]
    ) -> npt.NDArray[np.number]
```