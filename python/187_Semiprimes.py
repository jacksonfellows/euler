from math import sqrt
import sympy
from bisect import bisect

def p187(N):
    s = 0
    primes = list(sympy.sieve.primerange(2, N // 2 + 1))
    for i,p in enumerate(primes):
        if p > sqrt(N):
            break
        j = bisect(primes, N // p)
        s += j - i
    return s
