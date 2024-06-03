# Task

You are given a set of vectors as basis that are stored
in a row-matrix `numpy.ndarray` $B$ and some some vector $x$.

It is guaranteed that the vector $x$ comes from
the span of the $B$ vectors. Find **covariant** coordinates
of vector $x$ in this $B$.

## Interface

```
def get_covariant_coordinates(B, x) -> res
```