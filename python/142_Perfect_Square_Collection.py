from math import isqrt


def ispsquare(x):
    n = isqrt(x)
    return n*n == x

def p():
    for z in range(1, 10**6):
        for i in range(1, 10**3):
            y = z + i*i
            if ispsquare(y + z):
                for j in range(1, 10**3):
                    x = y + j*j
                    if ispsquare(x + y) and ispsquare(x + z) and ispsquare(x - z):
                        print(x, y, z)
                        return x + y + z
