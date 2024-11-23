from collections import Counter

from sympy import factorint


def p():
    n = 20_000_000
    k = 15_000_000
    factors = Counter()
    for i in range(k+1, n+1):
        for f,c in factorint(i).items():
            factors[f] += c
    for j in range(1, n-k+1):
        for f,c in factorint(j).items():
            factors[f] -= c
    s = 0
    for f,c in factors.items():
        s += f*c
    return s
