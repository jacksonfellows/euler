from math import *

def shortest_path(a, b, c):
    # assumes a > b and a > c
    return sqrt(a**2 + (b + c)**2)

def is_integer(x):
    return x == int(x)

from itertools import *

def n_integer(M):
    n = 0
    for c in combinations_with_replacement(range(1,M+1), 3):
        if is_integer(shortest_path(*reversed(c))):
            # yield(tuple(reversed(c)))
            n += 1
    return n

def n_integer_2(M):
    n = 0
    for a in range(1, M + 1):
        for b_c in range(1, 2*a + 1):
            if is_integer(sqrt(a**2 + b_c**2)):
                # for c in range(1 if b_c < min(a, M) else b_c - min(a, M), b_c // 2 + 1):
                #     b = b_c - c
                #     yield((a, b, c))
                n += b_c // 2 + 1 - (1 if b_c < min(a, M) else b_c - min(a, M))
    return n

def find_first_gt(M_l, M_h, N, depth = 0):
    if depth >= 10:
        return M_l, M_h
    M_mid = M_l + (M_h - M_l) // 2
    n = n_integer_2(M_mid)
    print(f'low = {M_l}, high = {M_h}, mid = {M_mid}, n = {n}')
    if n < N:
        return find_first_gt(M_mid, M_h, N, depth + 1)
    else:
        return find_first_gt(M_l, M_mid, N, depth + 1)
