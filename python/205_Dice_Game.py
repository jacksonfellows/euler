from itertools import product
from collections import Counter

def die_dist(faces, n_rolls):
    counter = Counter()
    for xs in product(faces, repeat=n_rolls):
        counter[sum(xs)] += 1
    return counter

def p205():
    P = die_dist(range(1,5), 9)
    C = die_dist(range(1,7), 6)
    P_total = sum(P.values())
    C_total = sum(C.values())
    P_wins = 0
    for P_roll, P_n in P.items():
        for C_roll, C_n in C.items():
            if C_roll < P_roll:
                P_wins += P_n / P_total * C_n / C_total
    return round(P_wins, 7)
