from functools import lru_cache
from math import isqrt

@lru_cache(None)
def n_divs(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n % 2 == 0:
        n //= 2
        c = 1
        while n % 2 == 0:
            c += 1
            n //= 2
        return (c + 1) * n_divs(n)
    for i in range(3,isqrt(n)+1,2):
        if n % i == 0:
            n //= i
            c = 1
            while n % i == 0:
                c += 1
                n //= i
            return (c + 1) * n_divs(n)
    return 2

def p179():
    last = 1
    n = 0
    for i in range(2,10000001):
        curr = n_divs(i)
        if curr == last:
            n += 1
        last = curr
    return n

print(p179())
