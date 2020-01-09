#/usr/bin/env python3
"""
This file generates smooth numbers — product of n consecutive primes with all possible exponents permutations
"""
import itertools
from functools import lru_cache
from sage.all import Primes, product
import tqdm

def generate_smooths(primes, max_power):
    @lru_cache(maxsize=None)
    def pow_cached(x, y, n=None):
        return pow(x, y, n)  

    primes_sorted = sorted(primes)
    for mask in itertools.product(range(max_power), repeat=len(primes_sorted)):
        yield product(list(map(pow_cached, primes_sorted, mask)))
    
if __name__ == "__main__":
    n = 5 # i
    max_power = 10 # max(e_i)
    max_prime = 1000 # max(p_i)

    # Geneate last n primes < max_prime
    P = Primes()
    primes = []
    t = P.first()
    while t < max_prime:
        primes.append(t)
        t = P.next(primes[-1])
    primes = primes[-n:]

    gen = generate_smooths(primes, max_power)
    smooths = []
    for i in tqdm.tqdm(gen, total=max_power**n):
        smooths.append(i)

    print(smooths[-10:])
