# Vectorized operations

In `numpy` the summation of the vectors luckily is already
implemented. Moreover, it is done using `C++` compiler, thus
the hardware-specific optimisation is applied to this operation,
and it will be performed in a **vectorized** manner.

What does the **vectorisation** imply?

That mean that the data will be loaded to the CPU cashes
and registers in batches that will massively speedup
the calculation.

One of the reasons of this speedup is that without 
vectorisation you only are capable of performing
one operation per CPU tick, but with vectorisation you
can perform several operations per tick.

There is another important reason: CPU works with RAM through
a sequence of caches. The caches that are closer to the
CPU load information faster, but have lower capacity. In
the same time, loading full cache of data takes almost the same
time as loading a single datum.

All of this is taken care by `C++` compiler that optimizes
the procedure cleverly. `Python` can not perform this
optimization as it performs interpretation of the code
instead of compilation. (Actually there still is a way,
but it still is under construction, see `PyPy` if you are
interested)

That means that loading data from RAM to caches in batches
should give us a massive speedup.

## Task

You are given two `numpy.ndarray`-s of the same shape. 
Your task is to sum these two arrays. 
You have to do that using the numpy summation: ```x + y```.
Note the execution time and compare it with previous task.

## Interface

**Inputs**: `x: numpy.ndarray`, `y: numpy.ndarray`.

**Outputs**: `z: numpy.ndarray`

## Conclusion

You should have 100x speedup! WOW...

Hence, one should by all means use the vectorized operations 
that
are optimized for your hardware and avoid cycling through the
`numpy.ndarray`. Probably everyone heard
rumors about Python inefficiency. That is the way to deal
with it!