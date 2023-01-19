#       21
#      49
#     56
#    35
#    7
#
#    111   -> carry
#   111111

# need an example with more digits:

#      41
#    287
#    82
#
#    11
#   11111

def make_last_digit(n, digit):
    # returns n*k s.t. (n*k)%10 == digit
    k = 0
    while (n*k) % 10 != digit:
        k += 1
    return n*k

def make_rep(n):
    # print(f'make_rep({n})')
    # pdb.set_trace()
    # find way to multiply n to get a repunit
    terms = [make_last_digit(n, 1)]
    n_digits = 1
    carry = 0
    # print(terms[0])
    while True:
        # shift terms
        terms = [term // 10 for term in terms if term // 10 != 0]
        if len(terms) == 0:
            return n_digits + 1
        # see what digit we need
        s = sum(term % 10 for term in terms)
        # want (s + carry + digit) % 10 == 1
        digit = (10 - (s + carry) % 10 + 1) % 10
        carry = (s + carry + digit) // 10
        new_term = make_last_digit(n, digit)
        # print(new_term * 10**n_digits)
        terms.append(new_term)
        n_digits += 1

import math

def p129(start, lim):
    n = start
    while True:
        r = make_rep(n)
        print(n, r)
        if r > lim:
            return n
        n += 1
        while math.gcd(n, 10) != 1:
            n += 1
