mat = [[int(n) for n in line.strip().split(',')] for line in open('../p081_matrix.txt').readlines()]

test_mat = [
    [131,673,234,103,18],
    [201,96,342,965,150],
    [630,803,746,422,111],
    [537,699,497,121,956],
    [805,732,524,37,331]
]

from functools import lru_cache

def min_path_sum(m):
    @lru_cache(None)
    def go(r, c):
        if r == len(m)-1 and c == len(m[0])-1:
            return m[r][c]
        if r == len(m)-1:
            return m[r][c] + go(r, c+1)
        if c == len(m[0])-1:
            return m[r][c] + go(r+1, c)
        return m[r][c] + min(go(r, c+1),
                             go(r+1, c))
    return go(0,0)

print(min_path_sum(mat))
