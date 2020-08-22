from functools import lru_cache
from math import isqrt

@lru_cache(None)
def prime_factors(n):
    for i in range(2,isqrt(n)+1):
        if n % i == 0:
            return (i,) + prime_factors(n // i)
    return (n,)

@lru_cache(None)
def sum_proper_divisors(n):
    if n < 2:
        return 0
    factors = prime_factors(n)
    i = 0
    s = 1
    while i < len(factors):
        start = factors[i]
        term = 1
        exp = 1
        while i < len(factors) and factors[i] == start:
            term += start**exp
            exp += 1
            i += 1
        s *= term
    return s - n

def find_chain_len(n):
    chain = [n]
    n = sum_proper_divisors(n)
    while n not in chain:
        if n > 1000000:
            return (None,0)
        chain.append(n)
        n = sum_proper_divisors(n)
    return (n, len(chain) - chain.index(n))

def p95():
    max_l = 0
    for i in range(1000000):
        n, l = find_chain_len(i)
        if l > max_l:
            max_l = l
            max_n = n
    return max_n, max_l

print(p95())
