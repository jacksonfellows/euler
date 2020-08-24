import gmpy2

def pandigital(n):
    return sorted(str(n)) == ['1','2','3','4','5','6','7','8','9']

def p104():
    a = b = gmpy2.mpz(1)
    n = 1
    while 1:
        if n % 10000 == 0:
            print(n)
        if pandigital(a // 10**(a.num_digits() - 9)) and pandigital(a % 1000000000):
            return n
        a, b = b, a + b
        n += 1

print(p104())
