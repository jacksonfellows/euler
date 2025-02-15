from functools import cache


@cache
def rec(last_digit, n, remaining):
    if n == 0:
        return len(remaining) == 0
    tot = 0
    if last_digit > 0:
        tot += rec(last_digit-1, n-1, remaining - {last_digit-1})
    if last_digit < 9:
        tot += rec(last_digit+1, n-1, remaining - {last_digit+1})
    return tot

def p(ndigits):
    tot = 0
    for n in range(1, ndigits+1):
        tot += sum(rec(digit, n-1, frozenset(range(10)) - {digit}) for digit in range(1,10))
    return tot

assert p(10) == 1