from functools import cache
from math import isqrt


@cache
def dr(n):
    if n < 10:
        return n
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    return dr(s)

@cache
def mdrs(n, min_factor=2):
    mdr = dr(n)
    for i in range(min_factor, isqrt(n) + 1):
        if n % i == 0:
            mdr = max(mdr, dr(i) + mdrs(n // i, i))
    return mdr

def p159(n):
    return sum(mdrs(n) for n in range(2, n))
