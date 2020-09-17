from math import isqrt

def cont_frac(d):
    r = isqrt(d)
    yield r
    a, p, q = r, 0, 1
    while 1:
        p = a*q - p
        q = (d - p*p)//q
        a = (r + p)//q
        yield a

def convergents(terms):
    p_1, q_1 = 1, 0
    p_2, q_2 = 0, 1
    for term in terms:
        p_k = term * p_1 + p_2
        q_k = term * q_1 + q_2
        yield (p_k, q_k)
        p_1, p_2 = p_k, p_1
        q_1, q_2 = q_k, q_1

def min_x(d):
    i = isqrt(d)
    if i*i == d:
        return 0
    return next(x for x,y in convergents(cont_frac(d)) if x*x - d*y*y == 1)

def p66():
    return max(range(1001), key=min_x)
