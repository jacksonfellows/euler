import sympy

def p123():
    for n,p in enumerate(sympy.sieve.primerange(10**6), 1):
        r = (pow(p - 1, n, p*p) + pow(p + 1, n, p*p)) % (p*p)
        if r > 10**10:
            print(n,p)
            break
