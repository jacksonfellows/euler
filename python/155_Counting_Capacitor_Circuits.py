from fractions import Fraction
from functools import cache

base = Fraction(1, 1)

@cache
def Cs(n):
    if n == 1:
        return set([base])
    s = set()
    for a in range(1, n//2 + 1):
        b = n - a
        for C1 in Cs(a):
            for C2 in Cs(b):
                s.add(C1 + C2)
                s.add(1/(1/C1 + 1/C2))
    return s

def D(n):
    s = set()
    for n_ in range(1, n+1):
        s |= Cs(n_)
    return s
