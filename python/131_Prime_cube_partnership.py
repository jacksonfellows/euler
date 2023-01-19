import sympy

def is_cube(n):
    return round(n**(1/3))**3 == n

def brute():
    count = 0
    last_j = 1
    for p in sympy.sieve.primerange(10**6):
        for j in range(last_j,900):
            n = j**3
            if is_cube(n**3 + n**2 * p):
                print(f'{n}^3 + {n}^2 x {p} == {n**3+n**2*p}')
                count += 1
                last_j = j
                break
    return count
