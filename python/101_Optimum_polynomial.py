import numpy as np

def OP(k, terms):
    m = np.fromfunction(lambda i,j: (i+1)**(k-j-1), (k,k))
    return np.linalg.solve(m, terms[:k])

def p101():
    terms = np.fromfunction(lambda i: 1 - i + i**2 - i**3 + i**4 - i**5 + i**6 - i**7 + i**8 - i**9 + i**10, (20,))[1:]
    s = 0
    for k in range(1, 11):
        poly = OP(k, terms)
        poly_vals = np.polyval(poly, np.arange(1, terms.shape[0]+1))
        s += poly_vals[(terms - poly_vals) > 1e-4][0]
    return s
