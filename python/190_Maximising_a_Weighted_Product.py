import math

import numpy as np
import scipy
from matplotlib import pyplot as plt


# Try to solve by optimizing 1/P_m
def f(x, m):
    return 1/(math.prod(xx**(i+1) for i,xx in enumerate(x))*(m - np.sum(x))**m)

# floor(s(10)) = 4111 (should be 4112)
def s(m):
    r = scipy.optimize.minimize(f, np.ones(m - 1), m, bounds=[(1e-3, float("inf")) for _ in range(m - 1)])
    print(1/r.fun)
    return r.x

# Look for patterns.
def p():
    for m in range(2,15):
        x = s(m)
        print([*x, m - np.sum(x)])
        plt.plot(x, label=m)
    plt.legend()
    plt.show()

# m: m_1 m_2 ... m_n
# 2: 2/3 4/3
# 3: 1/2 2/2 3/2
# 4: 2/5 4/5 6/5 8/5
# 5: 1/3 2/3 3/3 4/3 5/3
# 6: 2/7 4/7 6/7 8/7 10/7 12/7
# 7: 1/4 1/2 3/4 4/4 5/4 6/4 8/4
# 8: 2/9 4/9 6/9 8/9 10/9 12/9 14/9 16/9
# 9: 1/5 2/5 3/5 4/5 5/5 6/5 7/5 8/5 9/5

# Guess the pattern:
def ms(m):
    if m % 2 == 0:
        d = m + 1
        return [n/d for n in range(2, m*2 + 1, 2)]
    else:
        d = m//2 + 1
        return [n/d for n in range(1, m+1)]

def Pm(m):
    return math.prod(x**n for x,n in zip(ms(m), range(1, m+1)))

def p190():
    return sum(math.floor(Pm(m)) for m in range(2, 15+1))
