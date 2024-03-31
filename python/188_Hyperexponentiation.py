def hyper(a, k, m):
    if k == 1:
        return a % m
    return pow(a, hyper(a, k-1, m), m)

def p188():
    return hyper(1777, 1855, 10**8)
