import math

# hopefully extend algorithm described at
# https://gist.github.com/dario2994/fb4713f252ca86c1254d to only
# generate square highly composite numbers
def find_square_hcns(primes):
    max_n = math.prod(primes)
    # list of (n, d(n), exponents of prime factors)
    hcns = [(1,1,[])]
    for i in range(len(primes)):
        new_hcns = []
        for hcn in hcns:
            new_hcns.append(hcn)
            if len(hcn[2]) < i:
                # if there already isn't a term for this prime do nothing
                continue
            # if i is 0, then find the max exponent for 2 (0th prime)
            # otherwise, we can't exceed the exponent for the previous prime factor
            exp_max = int(math.log(max_n, 2)) if i == 0 else hcn[2][i-1]
            n = hcn[0]
            # try each possible exponent for this prime
            for exp in range(2, exp_max+1, 2): # use step of 2 to keep number square?
                n *= primes[i] * primes[i]
                if n > max_n:
                    break
                n_divisors = hcn[1] * (exp+1)
                exponents = hcn[2] + [exp]
                new_hcns.append((n, n_divisors, exponents))
        new_hcns.sort()
        hcns = [(1,1,[])]
        # only keep the best hcn for each number
        for hcn in new_hcns:
            if hcn[1] > hcns[-1][1]:
                hcns.append(hcn)
    return hcns

import erat

def p110():
    # need surprisingly few primes
    return int(math.sqrt([a for a in find_square_hcns(erat.erat(100)[0]) if a[1]/2 > 4000000][0][0]))
