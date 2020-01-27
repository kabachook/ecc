# Singular curves

## Description

If a curve is a singular one (i.e. its discriminant $\Delta = -16(4a^3 + 27b^2) \mod p = 0$), it is isomorphic to multiplicative group, which enables to solve DLP faster.

## Task

Given arbitary curve $E$ with $\Delta = 0$, and some point $P = d*G$, find $d$.

## Solution

In case of $\Delta = 0$ the curve has double or triple root $x_{0}$ and the point $(x_{0}, 0)$ is a singular point.

With a change of variable, you can come to two cases:

1. Cusp $y^2 = x^3$

    The curve is isomorphic to *additive group* of $F_{p}$ (there is a mapping to that group), where discrete logarithm is trivial.

2. Node $y^2 = x^2*(x - 1)$

    The curve is isomorphic to *multiplicative group* of $\mathbf F_{p^2}^*$, where discrete logarithm is easier to compute.
    
## Links

- https://crypto.stackexchange.com/questions/61302/how-to-solve-this-ecdlp
- https://crypto.stackexchange.com/questions/70373/why-are-singular-elliptic-curves-bad-for-crypto