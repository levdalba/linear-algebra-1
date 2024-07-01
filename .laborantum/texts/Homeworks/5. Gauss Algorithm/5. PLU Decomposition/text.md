# PLU decomposition

You are given a square matrix $A$.

Using Gauss Algorithm Step 1, perform PLU 
decomposition (find matrices $P, L, U$, where $P$ is a permutation matrix, 
$L$ is an lower-triangle matrix and $U$ is an upper-triangle matrix.

## Hints

Imagine the process, you start with the SLE

$$A \mathbf x = I \mathbf b$$

First you perform the permutations so that Gauss Elimination Stage 1
runs stabilly

$$A' \mathbf x = P \mathbf b$$

One can add $I$ to the right hand side without changing the correctness:

$$A' \mathbf x = I P \mathbf b$$

Afterwards you perform Gauss Eliminaton Stage 1 (and yes, permutations you
actually perfrom during GE Stage 1, but if you knew them in advance, you
could have done them in advance)

$$U \mathbf x = L P \mathbf b$$

Now we can invert the matrices $L$ and $P$ and we will get in the end:

$$P' L' U \mathbf x = \mathbf b$$

That indicates $A = P' L' U$.

Note that $P' = P^T$ and $L' = L^{-1}$, and we know that $L^{-1}$ is a
lower-triangular matrix too, meaning that matrix $A$ can **always** be
decomposed into a product of:
* permutation matrix
* lower triangular matrix
* upper triangular matrix