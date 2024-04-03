from functools import cache

# t = [
#     [15],
#     [-14, -7],
#     [20, -13, -5],
#     [-3, 8, 23, -26],
#     [1, -4, -5, -18, 5],
#     [-16, 31, 2, 9, 28, 3],
# ]

def make_tri():
    tri = [[]]
    t = 0
    for k in range(500500):
        t = (615949*t + 797807) % 2**20
        sk = t - 2**19
        if len(tri) == 1:
            if len(tri[-1]) == 1:
                tri.append([])
            tri[-1].append(sk)
        else:
            if len(tri[-1]) > len(tri[-2]):
                tri.append([])
            tri[-1].append(sk)

    return tri

t = make_tri()

@cache
def trisums(row, col):
    if row >= len(t) or col >= len(t):
        return [0]
    if row == len(t) - 1 or col == len(t) - 1:
        return [t[row][col]]
    sums = []
    sum_ = t[row][col]
    sums.append(sum_)
    for a,b,c in zip(trisums(row + 1, col), [0] + trisums(row + 2, col + 1), trisums(row + 1, col + 1)):
        sums.append(sum_ + a + c - b)
    return sums

@cache
def minsum(row, col):
    if row == len(t) or col == len(t):
        return 0
    return min(*trisums(row, col), minsum(row + 1, col), minsum(row + 1, col + 1))
