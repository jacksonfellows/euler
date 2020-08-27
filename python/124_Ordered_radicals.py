from math import isqrt
from functools import lru_cache

@lru_cache(None)
def rad(n):
    for i in range(2, isqrt(n)+1):
        if n % i == 0:
            while n % i == 0:
                n //= i
            return i * rad(n)
    return n

def p124():
    return sorted((rad(n),n) for n in range(1,100001))[9999][1]

print(p124())
