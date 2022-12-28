from sympy import sieve
import collections

def get_prime_digit_counts(n):
    digits_to_n_primes = collections.Counter()
    for p in sieve.primerange(n):
        if len(set(str(p))) == len(str(p)) and '0' not in str(p):
            digits_to_n_primes[frozenset(map(int, str(p)))] += 1
    return digits_to_n_primes

import itertools

def find_prime_sets(counts):
    keys = tuple(counts.keys())
    n = 0
    for a in range(len(counts)):
        if len(keys[a]) == 9:
            n += counts[keys[a]]
            # print(counts[keys[a]])
        else:
            for b in range(a+1, len(counts)):
                if keys[a] & keys[b] == set():
                    if len(keys[a]) + len(keys[b]) == 9:
                        n += counts[keys[a]] * counts[keys[b]]
                        # print(keys[a], keys[b])
                    else:
                        for c in range(b+1, len(counts)):
                            if (keys[a] | keys[b]) & keys[c] == set():
                                if len(keys[a]) + len(keys[b]) + len(keys[c]) == 9:
                                    n += counts[keys[a]] * counts[keys[b]] * counts[keys[c]]
                                    # print(keys[a], keys[b], keys[c])
                                else:
                                    for d in range(c+1, len(counts)):
                                        if (keys[a] | keys[b] | keys[c]) & keys[d] == set():
                                            if len(keys[a]) + len(keys[b]) + len(keys[c]) + len(keys[d]) == 9:
                                                n += counts[keys[a]] * counts[keys[b]] * counts[keys[c]] * counts[keys[d]]
                                                # print(keys[a], keys[b], keys[c], keys[d])
                                            else:
                                                for e in range(d+1, len(counts)):
                                                    if (keys[a] | keys[b] | keys[c] | keys[d]) & keys[e] == set():
                                                        if len(keys[a]) + len(keys[b]) + len(keys[c]) + len(keys[d]) + len(keys[e]) == 9:
                                                            n += counts[keys[a]] * counts[keys[b]] * counts[keys[c]] * counts[keys[d]] * counts[keys[e]]
                                                            # print(keys[a], keys[b], keys[c], keys[d], keys[e])
                                                        else:
                                                            for f in range(e+1, len(counts)):
                                                                if (keys[a] | keys[b] | keys[c] | keys[d] | keys[e]) & keys[f] == set():
                                                                    if len(keys[a]) + len(keys[b]) + len(keys[c]) + len(keys[d]) + len(keys[e]) + len(keys[f]) == 9:
                                                                        n += counts[keys[a]] * counts[keys[b]] * counts[keys[c]] * counts[keys[d]] * counts[keys[e]] * counts[keys[f]]
                                                                        # print(keys[a], keys[b], keys[c], keys[d], keys[e], keys[f])

    return n
