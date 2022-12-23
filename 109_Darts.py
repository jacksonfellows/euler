singles = [*range(1,21), 25]
doubles = [*range(1,21), 25]
triples = [*range(1,21)]

def checkouts_(score, n):
    if score == 0:
        return [()]
    if n == 3:
        return []
    res = []
    for x in singles:
        if x > score: break
        res += [(*r,f's{x}') for r in checkouts_(score - x, n+1)]
    for x in doubles:
        if 2*x > score: break
        res += [(*r,f'd{x}') for r in checkouts_(score - 2*x, n+1)]
    for x in triples:
        if 3*x > score: break
        res += [(*r,f't{x}') for r in checkouts_(score - 3*x, n+1)]
    return res

def checkouts(score):
    # have to end on a double
    res = []
    for x in doubles:
        if 2*x > score: break
        res += [(*r,f'd{x}') for r in set(tuple(sorted(c)) for c in checkouts_(score - 2*x, 1))]
    return res

def p109():
    s = 0
    for n in range(1,100):
        s += len(checkouts(n))
    return s
