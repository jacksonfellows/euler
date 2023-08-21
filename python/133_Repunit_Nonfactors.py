from itertools import count
from sympy import primefactors, primerange

def prime_can_divide(divisor):
    x = 0
    first_x = None
    last_x = None
    for i in count(0):
        x = 10 * ((x + 1) % divisor)
        if x == first_x:
            return last_x == 0 and set(primefactors(i)) <= {2, 5}
        if i == 0:
            first_x = x
        last_x = x

def p133():
    S = 0
    for p in primerange(2, 100_000):
        if not prime_can_divide(p):
            S += p
        else:
            print(f"{p} can divide")
    return S
