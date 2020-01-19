# Pohlig-Hellman algorithm

## Task

Given arbitary curve with [smooth](https://en.wikipedia.org/wiki/Smooth_number) order and some point P = d*G, find d.

## Solution

This is a general ECDLP problem, but it can be simplified using Pohlig-Hellman algorithm, which restates the problem of finding ECDLP in n-order group to finding ECDLP in groups with order of n divisors.

Then after applying [CRT](https://en.wikipedia.org/wiki/Chinese_remainder_theorem) to equations k = k_i mod p_i^e_i we find k.

![](https://upload.wikimedia.org/wikipedia/commons/6/66/Pohlig-Hellman-Diagram.svg)

## Links

https://en.wikipedia.org/wiki/Pohlig%E2%80%93Hellman_algorithm
https://koclab.cs.ucsb.edu/teaching/ecc/project/2015Projects/Sommerseth+Hoeiland.pdf