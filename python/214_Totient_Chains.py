from functools import cache
from math import isqrt

from sympy import primerange, totient

chain_len_cache = {1: 1}

def chain_len(n):
    n_ = n
    for l in range(25):
        if n_ in chain_len_cache:
            chain_len_cache[n] = l + chain_len_cache[n_]
            return chain_len_cache[n]
        n_ = totient(n_)
    chain_len_cache[n] = -1
    return -1

def p214():
    S = 0
    for p in primerange(40_000_000):
        if chain_len(p) == 25:
            # print(p)
            S += p
    return S
