import functools

@functools.cache
def n_ways(tile_len, l):
    if l <= 0:
        return 1
    return (n_ways(tile_len, l - tile_len) if tile_len <= l else 0) + n_ways(tile_len, l - 1)

def p116():
    return sum(n_ways(t, 50)-1 for t in (2,3,4))
