from functools import cache


# Same approach as Haskell solution.
@cache
def p(n, xs):
    if len(xs) == 1: return int(not (n % xs[0]))
    return sum(p(n - d*xs[0], xs[1:]) for d in range(0, n // xs[0] + 1))

def p31():
    return p(200, (1,2,5,10,20,50,100,200))
