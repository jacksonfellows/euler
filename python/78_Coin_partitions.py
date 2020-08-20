from math import sqrt
from functools import lru_cache

@lru_cache(None)
def p(n):
    if n == 0:
        return 1
    s = 0
    lower = int(-(sqrt(24*n+1)-1)/6)
    upper = int((sqrt(24*n+1)+1)/6)
    for k in range(lower, upper+1):
        if k == 0:
            continue
        v = p(n - k*(3*k - 1)//2)
        if k % 2 == 0:
            s -= v
        else:
            s += v
    return s

def p78():
    n = 0
    while 1:
        if p(n) % 1000000 == 0:
            return n
        n += 1

print(p78())
