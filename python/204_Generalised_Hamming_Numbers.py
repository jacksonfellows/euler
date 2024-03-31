import sympy

P = list(sympy.primerange(100))

def hammings_under(primes, lim, n):
    if len(primes) == 0:
        return 1
    p = primes[0]
    S = 0
    for k in range(lim):
        n_ = n*p**k
        if n_ > lim:
            break
        S += hammings_under(primes[1:], lim, n_)
    return S

def p204():
    return hammings_under(P, 10**9, 1)
