from math import isqrt

import sympy


def is_prime(n):
    return sympy.isprime(n)

def check(n):
    for d in range(1, isqrt(n)+1):
        if n % d == 0:
            if not is_prime(d + n // d):
                return False
    return True

def p357():
    return sum(n for n in range(100_000_000) if check(n))
