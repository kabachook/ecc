# Pohlig-Hellman algorithm

## Description

If group order is not a prime number, but a smooth one with little factors, the ECDLP problem can be solved in less time.
Instead of $O(\sqrt{n})$,  $O(\sum e_i*(\log{n} + \sqrt{p_{i}}))$. Where $n = \prod p_{i}^{e_{i}}$

## Task

Given arbitary curve $E$ with [smooth](https://en.wikipedia.org/wiki/Smooth_number) order and some point $P = d*G$, find $d$.

## Solution

This is a general ECDLP problem, but it can be simplified using Pohlig-Hellman algorithm, which restates the problem of finding ECDLP in $n$-order group to finding ECDLP in groups with order of divisors of $n$.

Then after applying [CRT](https://en.wikipedia.org/wiki/Chinese_remainder_theorem) to equations $k = k_{i} \mod p_{i}^{e_{i}}$ we find $k$.

![](https://upload.wikimedia.org/wikipedia/commons/6/66/Pohlig-Hellman-Diagram.svg)

## How to generate task

```bash
./gen_task.sh > >(tee task.txt) 2> >(tee log.txt >&2)
```

You will get two files:

- `task.txt` — task itself
- `log.txt` — task generator log with answer

## Links

- https://en.wikipedia.org/wiki/Pohlig%E2%80%93Hellman_algorithm
- https://koclab.cs.ucsb.edu/teaching/ecc/project/2015Projects/Sommerseth+Hoeiland.pdf