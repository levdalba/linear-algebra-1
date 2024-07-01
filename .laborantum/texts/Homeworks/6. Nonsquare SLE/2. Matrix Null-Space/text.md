# Null-space of a Matrix

You are given a matrix $A$.

Write a program to find the null space of this matrix using Gaussian Elimination Stage 1.

In the answer, enumerate the basis  vectors of kernel in the order they appear in the matrix after Gaussian Elimination Stage 1.

## Hints

Your Gauss Elimination Steps 1 and 2 should be able to deal with
non-square matrices.

After Gauss Elimination Step 1, get rid of zero rows and
permute the columns so that you have a full non-zero main diagonal.
In that case Gauss Elimination Step 2 will not cause troubles.

Note that permuting the columns means that you permute the 
coordinates of $\mathbf x$. You should permute them backward
afterwards.

Keep the order of the kernel vectors.

The Null-Space of $A$ should be given as a matrix $B$ so that
$AB = 0$.