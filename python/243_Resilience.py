from math import gcd, prod
from functools import cache
from sympy import factorint
from itertools import combinations

goal_R = 15499 / 94744

def R_1(d):
    n_res = 0
    for n in range(1,d):
        if gcd(n, d) == 1:
            n_res += 1
    return n_res / (d - 1)

def R_2(d):
    factors = list(factorint(d).keys())
    n_cancel = 0
    for r in range(1,len(factors)+1):
        for xs in combinations(factors, r=r):
            n_cancel -= (-1) ** r * d // prod(xs)
    return (d - n_cancel) / (d - 1)

def search_R(N):
    best_R = float('inf')
    A = 2*3*5*7*11*13*17
    for x in range(2,N//A):
        d = A*x
        R = R_2(d)
        if R < best_R:
            print(f"{d=}, {R=}, factors={factorint(d)}")
            if R < goal_R:
                break
            best_R = R
    return best_R
