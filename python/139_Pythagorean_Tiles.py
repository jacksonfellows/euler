from itertools import count
from math import gcd


def triples(lim):
    for n in count(1):
        if ((n+1)*(n+1) - n*n) + (2*(n+1)*n) + ((n+1)*(n+1) + n*n) > lim:
            break
        for m in count(n+1):
            if (m*m - n*n) + (2*m*n) + (m*m + n*n) > lim:
                break
            if gcd(n,m) != 1:
                continue
            if (n % 2 == 1) and (m % 2 == 1):
                continue
            for k in count(1):
                a = k*(m*m - n*n)
                b = k*(2*m*n)
                c = k*(m*m + n*n)
                if a + b + c > lim:
                    break
                if a > b:
                    a,b = b,a
                assert a**2 + b**2 == c**2
                assert a < b < c
                yield a,b,c

def p139():
    count = 0
    for a,b,c in triples(int(1e8)):
        if c%(b-a)==0:
            # print(a,b,c)
            count += 1
    return count
