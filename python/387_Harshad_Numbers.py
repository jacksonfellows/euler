import sympy


def is_right_harshad(n):
    if n < 10: return True
    digit_sum = sum(int(x) for x in str(n))
    return n % digit_sum == 0 and is_right_harshad(n // 10)

# --------------------------------------------------------------------------------

def add_digit(n, dsum):
    for d in range(10):
        if (n*10 + d)%(dsum + d) == 0:
            yield n*10 + d, dsum + d

def gen_harshads():
    harshads = zip(list(range(1,10)), list(range(1,10)))
    while 1:
        new_harshads = []
        for n,dsum in harshads:
            yield n,dsum
            for new in add_digit(n,dsum):
                new_harshads.append(new)
        harshads = new_harshads

def harshads_under(lim):
    for n,dsum in gen_harshads():
        if n < lim: yield n,dsum
        else: return

def p(lim):
    s = 0
    for h,dsum in harshads_under(lim//10):
        if sympy.isprime(h//dsum):    # Strong
            # Look for primes with h as left digits:
            for d in range(10):
                p = h*10 + d
                if sympy.isprime(p) and p < lim:
                    s += p
    return s
