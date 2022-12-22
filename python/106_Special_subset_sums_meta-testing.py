import itertools

def disjoint_pairs(m, n):
    S = set()
    s = set(range(m))
    for a in itertools.combinations(s, n):
        for b in itertools.combinations(s - set(a), n):
            S.add(tuple(sorted((a,b))))
    return S

def n_work(m, n):
    N = 0
    for a,b in disjoint_pairs(m, n):
        if not all(y > x for x,y in zip(a,b)):
            N += 1
    return N

def p106():
    return sum(n_work(12,n) for n in range(12))
