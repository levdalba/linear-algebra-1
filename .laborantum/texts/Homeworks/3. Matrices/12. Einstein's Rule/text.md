# Einstein's Rule

In *Tensor Algebra*, a direct generalization of the Linear Algebra to the case of $N$-dimentional tables called *tensors* (normal matrix), the Einstein's rule exists.

It works as follows: if you see a duplicating upper and lower index in the formula, that means, this index convolves.

For example, the following tensor expression, summation and matrix product are equivalent:

$$a_k^l b_l^m = \sum_{l=1}^L a_k^l b_l^m = AB$$

In this notation subscript means row index and superscript means column index.

<details>
<summary> Note </summary>

> [!NOTE]
> Also at some point it will be important to know that:
> * lower index represents a contravariant dimension of a
> tensor
> * upper index represents a covariant dimension 
> of tensor. But let us omit this part for now.

</details>

# Task

Calculate the following expression written using Einstein's 
rule:

$$a_k^m b_m^n c_n^o d_l^k$$