from math import *

def pandigital(n):
    return sorted(str(n)) == ['1','2','3','4','5','6','7','8','9']

def p104():
    a = b = 1
    n = 1
    logPhi = log10(1 + sqrt(5)) - log10(2)
    logF = logPhi - log10(sqrt(5))
    while 1:
        if pandigital(a) and pandigital(int(exp(log(10)*logF)*1e8)):
            return n
        a, b = b, (a + b)%1000000000
        logF = (logF + logPhi)%1
        n += 1

print(p104())
