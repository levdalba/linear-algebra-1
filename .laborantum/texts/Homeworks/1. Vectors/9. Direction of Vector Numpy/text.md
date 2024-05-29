# Direction of Vector Numpy
## What you may need

One can create a deep copy of `numpy.ndarray` (i.e., a separate
complete duplicate entity) using `x.copy()` method.

One can also reassign a coordinate of a vector using the
normal assignment procedure `x[index] = 2`

Note that in case you have done a shallow copy of a 
`numpy.ndarray`, then after the assignment, the original
entity will also change (as the second entity is nothing
but a link to the original entity).

Example:
Shallow copy
```python
import numpy

x = numpy.array([1, 2, 3])
y = x
y[1] = 5
print(y) # [1, 5, 3]
print(x) # [1, 5, 3] 
```

Deep copy
```python
import numpy

x = numpy.array([1, 2, 3])
y = x.copy()
y[1] = 5
print(y) # [1, 5, 3]
print(x) # [1, 2, 3] 
```

## Task

You are given a vector `x` as a `numpy.ndarray`. Return
its direction (i.e., a unit vector pointing in the same
direction as the original). To do so, create a deep copy
of the original vector and reassign its coordinates.

## Interface
```python
def vector_direction(x: npt.NDArray[np.number]) -> npt.NDArray[np.number]
```

### Inputs
`x: npt.NDArray[np.number]`

### Outputs 
`l: npt.NDArray[np.number]`