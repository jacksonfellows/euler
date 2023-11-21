# Copied from 173.

from collections import Counter
from math import prod

from sympy import factorint


def f(N):
    counts = Counter()
    for n in range(8,N+1,4):
         counts[prod(c+1 for c in factorint(n//4).values()) // 2] += 1
    return counts

def p174():
    return sum(c for n,c in f(int(1e6)).items() if n <= 10)
