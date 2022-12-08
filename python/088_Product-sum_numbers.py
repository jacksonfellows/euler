from math import *

def incr_index(tup, i):
    return tuple(x + 1 if i == j else x for j,x in enumerate(tup))

def find_product_sum(k):
    states = set(((1,) * k,))
    while True:
        states_tmp = states
        states = set()
        print(f'gen ({len(states_tmp)})')
        for t in states_tmp:
            i = None
            for j in range(len(t) - 1, -1, -1):
                if t[j] < t[len(t) - 1]:
                    i = j
                    break
            if i is not None:
                t_ = incr_index(t, i)
                if sum(t_) == prod(t_):
                    return sum(t_)
                if sum(t_) > prod(t_):
                    states.add(t_)
            t_ = incr_index(t, len(t) - 1)
            if sum(t_) == prod(t_):
                return sum(t_)
            if sum(t_) > prod(t_):
                states.add(t_)

def p88(N):
    total_set = set()
    for k in range(2, N + 1):
        print(f'k: {k}')
        n = find_product_sum(k)
        print(f'n: {n}')
        total_set.add(n)
    return sum(total_set)
