import math
from fractions import Fraction

from sympy import primefactors


def M(N):
    k = N / math.e
    # Could round either way.
    k_low = math.floor(k)
    k_high = math.ceil(k)
    return max(Fraction(N,k_low)**k_low, Fraction(N,k_high)**k_high)

def D(N):
    m = M(N)
    return -N if set(primefactors(m.denominator)) <= {2,5} else N

def p183():
    return sum(D(N) for N in range(5, 10001))
