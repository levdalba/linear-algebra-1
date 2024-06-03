# Checking linear independency

You are given a set of vectors in form of list
of `numpy.array`-s.

Your task is to return a boolean value indicating whether
the set of vectors is linearly dependent or not.

## Hint

In case the set of vectors is linearly independent,
the orthogonalisation procedure will always yield
a non-zero vector.

Otherwize sooner or later the orthogonalisation procedure
will yield a zero vector.

# Task

Code the function that determines whether the set of
vectors is linearly independent.

# Interface

```
def is_independent(A) -> bool
```