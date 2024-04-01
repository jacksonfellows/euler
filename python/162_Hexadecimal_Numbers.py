from functools import cache


@cache
def nhex(n, n0, n1, nA):
    S = 0
    if n0 >= 1 and n1 >= 1 and nA >= 1:
        S += 1
    if n == 16: return S
    if n != 0:
        S += nhex(n + 1, n0 + 1, n1, nA)
    S += nhex(n + 1, n0, n1 + 1, nA)
    S += nhex(n + 1, n0, n1, nA + 1)
    S += 13*nhex(n + 1, n0, n1, nA)
    return S

def p162():
    return hex(nhex(0, 0, 0, 0))[2:].upper()
