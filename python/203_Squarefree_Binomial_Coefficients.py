import math


def pascals_distinct(n):
    d = set()
    x = [1]
    for _ in range(n):
        d.update(x)
        x = [a + b for a,b in zip([*x,0], [0,*x])]
    return d

def squarefree(n):
    i = 2
    while i <= math.isqrt(n):
        if n % i == 0:
            n //= i
            if n % i == 0:
                return False
        i += 1
    return True

def p203():
    return sum(x for x in pascals_distinct(51) if squarefree(x))
