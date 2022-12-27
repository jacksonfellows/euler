import functools

@functools.cache
def n_ways(l):
    if l <= 0:
        return 1
    s = 0
    for tile_len in (2,3,4):
        if tile_len <= l:
            s += n_ways(l - tile_len)
    s += n_ways(l - 1)
    return s

def p117():
    return n_ways(50)
