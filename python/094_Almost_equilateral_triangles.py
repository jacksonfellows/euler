from math import sqrt, gcd
from itertools import count

def p94(max_P):
    P = 0
    max_N = int(sqrt(max_P / 4))
    for m in range(1, max_N + 1):
        for n in range(m + 1, max_N + 1):
            if gcd(m, n) == 1 and m % 2 != n % 2:
                for k in count(1):
                    a = k * (n*n - m*m)
                    b = k * 2 * m * n
                    c = k * (n*n + m*m)
                    if (2*a + 2*c) > max_P:
                        break
                    if c == 2*a - 1 or c == 2*a + 1:
                        print(c, c, 2 * a)
                        P += 2*a + 2*c
                    if c == 2*b - 1 or c == 2*b + 1:
                        print(c, c, 2 * b)
                        P += 2*b + 2*c
    return P
