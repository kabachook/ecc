#!/usr/bin/env python3
"""
This file generates smooth numbers — product of n consecutive primes with all possible exponents permutations
Q = product(p_i^e_i)
"""
import itertools
from functools import lru_cache
from collections import deque
from sage.all import Primes, product

def generate_smooths(primes, max_power, reverse=False):
    "Returns generator of smooth numbers in form of product(primes_i^e), where e in range(0, max_power)"
    @lru_cache(maxsize=None)
    def pow_cached(x, y, n=None):
        return pow(x, y, n)  

    primes_sorted = sorted(primes)

    powers = range(max_power)
    if reverse:
        powers = reversed(powers)

    for mask in itertools.product(powers, repeat=len(primes_sorted)):
        yield product(list(map(pow_cached, primes_sorted, mask)))

def primes_less_than_n(n, count):
    "Generate last `count` primes < n"
    P = Primes()
    primes = deque(maxlen=count)
    t = P.first()
    while t < n:
        primes.append(t)
        t = P.next(t)
    return list(primes)


if __name__ == "__main__":
    import tqdm
    n = 5 # i
    max_power = 10 # max(e_i)
    max_prime = 10000000 # max(p_i)

    # Geneate last n primes < max_prime
    primes = primes_less_than_n(max_prime, n)    

    gen = generate_smooths(primes, max_power)
    smooths = []
    for i in tqdm.tqdm(gen, total=max_power**n):
        smooths.append(i)

    print(smooths[-10:])
