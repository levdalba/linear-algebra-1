# Length of Vector with Numpy

## About Numpy vector indexing
`numpy` arrays hold values of the same type. The type of
the values within `numpy.array` can be accessed using the
`x.dtype` method, where `x` is the `numpy.ndarray`.

The values that are stored within `numpy.ndarray` can be
accessed using the common indexing just like the items of
`list` or `tuple`. For instance, in case 
`x = numpy.array([1.1, 1.2, 1.3, 1.4, 1.5])`, then
`x[3]` accesses the 3rd element of `x`. Note that indexing
of `numpy.ndarray` starts with zero, thus, `x[3]` refers to
a value `1.4`.

Also one can access the length of the vector using `len`
function just as we do that with `list` and `tuple`.

## Task
Using the indexing procedure, write a function that
accepts as input a `numpy.ndarray` and returns its length.
To calculate a square root, use a function `numpy.sqrt`.

## Interface
```python
def vector_length(x: npt.NDArray[np.number]) -> float
```

### Inputs
`x: npt.NDArray[np.number]`

### Outputs 
`len_x: float`