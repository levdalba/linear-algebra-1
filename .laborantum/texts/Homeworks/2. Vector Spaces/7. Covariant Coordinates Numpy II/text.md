# Contravariate Coordinates to Covariate Coordinates

<div class="alert alert-danger">

> [!CAUTION]
> **This task is hard** 
>
> It is **intended** that it takes time, effort and creativity to solve.
>
>If you experience troubles -- carry on with a course and
>consult with other students for hints and ideas.

It is time to start working with 3 dimensional arrays. That
might be useful when you want to speed up some calculations.

## Task

You are given a set of $N$ basis vectors in the form of row-matrix
$B$ of size $N \times M$ and a set of **contravariant** 
coordinates in that basis $C$ for $K$ vectors of
size $N \times K$. Your task is to calculate the **covariant**
coordinates in the same basis.

> [!WARNING]
> Use only vetorized operations in this task

<details>
<summary> <b>Hint 1</b> </summary>

> [!TIP]
> You should operate with definitions of covariant and
> contravariant coordinates.
>
> Covariate coordinates are easy to calculate, but harder to use
> in reconstruction:
>
> $$x_k^* = \left<\mathbf x, \mathbf e_k\right>,$$
>
> the contravariant coordinates meanwhile are responsible for
> reconstruction:
> 
> $$\mathbf x = \sum_{k=1}^N x_k \mathbf e_k.$$
>
> Inserting the second expression in the first, one can derive
> a relation between the covariant and contravariant 
> coordinates.
>
> From there you will see, how the covariant coordinates can be
> expressed via contravariant ones.
</details>

<details>
<summary> <b>Hint 2</b> </summary>

> [!TIP]
> This task is somewhat similar to the vector reconstruction
> from contravariant coordinates.
</details>

## Interface

**Inputs**: `basis: 2D numpy.ndarray`, `coords: 2D numpy.ndarray`

**Outputs**: `co_coords: 2D numpy.ndarray`