import functools

@functools.cache
def ways_to_fill(n):
    if n <= 0:
        return 1
    ways = 0
    for block_len in range(3,n+1):
        ways += ways_to_fill(n - block_len - 1)
    ways += ways_to_fill(n - 1)
    return ways
