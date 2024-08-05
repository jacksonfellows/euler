import sympy


def find_n(p1, p2):
    a = 1
    n_digits = len(str(p1))
    m = 10 ** n_digits
    while 1:
        n = a*p2
        if n % m == p1:
            return n
        a += 1

def find_n_2(p1, p2):
    carry = 0
    a_digits = []
    while p1 > 0:
        p1_d = p1 % 10
        p2_d = p2 % 10
        carry_d = carry % 10
        ds = [d for d in range(10) if (p2_d * d + carry_d) % 10 == p1_d]
        assert len(ds) == 1
        d = ds[0]
        carry += p2 * d
        a_digits.append(d)
        p1 //= 10
        carry //= 10
    a = int("".join(reversed(list(map(str, a_digits)))))
    return a*p2

def p134(lim=1_000_000):
    s = 0
    p1 = 5
    for p2 in sympy.sieve.primerange(7, lim+100):
        if p1 > lim: break
        S = find_n_2(p1, p2)
        # assert S == find_n(p1, p2)
        assert S % p2 == 0
        nd = len(str(p1))
        assert str(S)[-nd:] == str(p1)
        s += S
        p1 = p2
    return s
