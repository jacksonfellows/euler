import itertools

def all_subsets(S):
    for r in range(1, len(S) + 1):
        yield from itertools.combinations(S, r)

def is_sss(A):
    for B,C in itertools.product(all_subsets(A), repeat=2):
        B,C = set(B),set(C)
        if B & C == set():
            if sum(B) == sum(C) or (len(B) > len(C) and sum(B) <= sum(C)):
                return False
    return True

p105_sets = [tuple(int(x) for x in line.strip().split(',')) for line in open('../p105_sets.txt').readlines()]

def p105():
    r = 0
    for s in p105_sets:
        if is_sss(s):
            print(s)
            r += sum(s)
    return r
