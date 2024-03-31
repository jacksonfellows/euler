from functools import cache


@cache
def n_prize_strings(n_ca, n_l, n_rem):
    if n_ca >= 3 or n_l > 1:
        return 0
    if n_rem == 0:
        return 1
    o = n_prize_strings(0, n_l, n_rem - 1)
    a = n_prize_strings(n_ca + 1, n_l, n_rem - 1)
    l = n_prize_strings(0, n_l + 1, n_rem - 1)
    return o + a + l

def p191():
    return n_prize_strings(0, 0, 30)
