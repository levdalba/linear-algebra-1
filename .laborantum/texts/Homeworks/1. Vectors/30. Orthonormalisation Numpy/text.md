## Task

You are given a list of ```numpy.ndarray```, each of the
arrays contains a vector. Dimensionality of all the vectors
is the same.

Write a program that, 
based on the original set of vectors,
generates a set of orthonormal vectors.

If a vector turns into zero throughout the orthonormalization
procedure, do not add it to the resulting list.

Consider vectors with norm $< 10^{-4}$ to be zero.

**Use only vectorised operations**

**Iterate over the original vectors sequentially**

**Inputs**:
```vecs: list(numpy.ndarray)```

**Outputs**:
```res: list(numpy.ndarray)```