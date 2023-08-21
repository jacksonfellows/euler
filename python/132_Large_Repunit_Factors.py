import sympy

def divisible(N, divisor):
    x = 0
    first_x = None
    prev_x = None
    for i in range(N):
        x = 10 * ((x + 1) % divisor)
        if x == first_x:
            return prev_x == 0 and N % i == 0
        if i == 0:
            first_x = x
        prev_x = x
    return x == 0

def p132(N):
    n_found = 0
    S = 0
    for p in sympy.primerange(2, 200000):
        if divisible(N, p):
            print(p)
            S += p
            n_found += 1
            if n_found == 40:
                print("found 40")
                break
    return S
