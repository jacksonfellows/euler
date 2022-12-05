def find_sqrt_digits(N, n_digits):
    c = N                       # assume N < 100
    p = 0
    for _ in range(n_digits):
        x = next(x for x in range(9, -1, -1) if x*(20*p + x) <= c)
        y = x*(20*p + x)
        yield x
        p = 10*p + x
        c = 100 * (c - y)

from math import sqrt

def is_sqrt_rational(N):
    s = sqrt(N)
    return s == int(s)

def p80():
    return sum(sum(find_sqrt_digits(N, 100)) for N in range(2,100) if not is_sqrt_rational(N))
