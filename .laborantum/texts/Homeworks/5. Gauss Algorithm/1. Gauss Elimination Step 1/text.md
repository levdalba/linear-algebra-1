# Gauss Elimintaion Implementation Step 1

## Task

You are given left-hand side matrix $A$ (of any shape) and a righ-hand side matrix $B$ (of any shape).

Implement the first stage of Gauss Elimination algorithm.
Use Stable version of Gauss Elimination.

## Stable Gauss Elimination

Stable Gauss Algorithm implies that before eliminating a
column, you permute the current line with some other line
below so that the element with which you eleminate the other elemts in this column, has the maximal possible absolute value.

This way you avoid dividing by zero when performing the
elimination.

If there are no non-zero elements in the current column, skip the current column and switch to the next one. The task is to eliminate as many values as possible.

Note that permutations should be stored in a 
permutation matrix $P$.

For example, if you start with

$$A \mathbf x = B \mathbf y$$

and in the end you get

$$P U \mathbf x  = P L B \mathbf y,$$

where $P$ is a permutation matrix.

## Some hints

The algorithm should perform same linear combinations of
rows of both left-hand side and right-hand side matrices.

The algorithm should eliminate the lower triangle of the
left-hand side matrix and make the main diagonal of it
equal to 1 if that is possible

Note that all matrices should be converted to float in the beginning of the algorithm.