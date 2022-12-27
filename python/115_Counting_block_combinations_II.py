import functools

@functools.cache
def F(m, n):
    if n <= 0:
        return 1
    ways = 0
    for block_len in range(m,n+1):
        ways += F(m, n - block_len - 1)
    ways += F(m, n - 1)
    return ways

def p115():
    n = 50
    while F(50, n) < 1e6: n += 1
    return n
