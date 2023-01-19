def make_last_digit(n, digit):
    # returns n*k s.t. (n*k)%10 == digit
    k = 0
    while (n*k) % 10 != digit:
        k += 1
    return n*k

def A(n):
    # find way to multiply n to get a repunit
    terms = [make_last_digit(n, 1)]
    n_digits = 1
    carry = 0
    # print(terms[0])
    while True:
        # shift terms
        terms = [term // 10 for term in terms if term // 10 != 0]
        if len(terms) == 0:
            return n_digits + carry
        # see what digit we need
        s = sum(term % 10 for term in terms)
        # want (s + carry + digit) % 10 == 1
        digit = (10 - (s + carry) % 10 + 1) % 10
        carry = (s + carry + digit) // 10
        new_term = make_last_digit(n, digit)
        # print(new_term*10**n_digits)
        terms.append(new_term)
        n_digits += 1

import sympy
import math

def p130():
    n = 91
    s = 0
    found = 0
    while found < 25:
        A_n = A(n)
        if (n - 1) % A_n == 0:
            print(n)
            s += n
            found += 1
        n += 1
        while sympy.isprime(n) or math.gcd(n, 10) != 1:
            n += 1
    return s
