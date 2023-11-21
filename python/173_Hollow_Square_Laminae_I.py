from math import prod

from sympy import factorint

# (a + b)(a - b) == a**2 - b**2 == n.

# Since a,b are the same parity a + b and a - b are both even.
# Therefore n must be divisible by 4. We can then find the number of
# pairs x,y s.t. x*y == n to find the number of values of a,b that
# satisfy this equation.

def count_pairs_2(N):
    C = 0
    for n in range(8,N+1,4):
        C += prod(c+1 for c in factorint(n//4).values()) // 2
    return C

def p173():
    return count_pairs_2(int(1e6))
