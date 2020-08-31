from erat import erat

N = 50000000

primes = erat(int(N**0.5))[0]

def p87():
    uniqs = set()
    for a in primes:
        a_lim = (N-a**2)**(1/3)
        for b in primes:
            if b > a_lim:
                break
            b_lim = (N-a**2-b**3)**0.25
            for c in primes:
                if c > b_lim:
                    break
                x = a**2 + b**3 + c**4
                if x > N:
                    print(a, b, c, x)
                uniqs.add(x)
    return len(uniqs)

print(p87())
