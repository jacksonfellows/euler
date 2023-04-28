def max_adj_sum(A):
    best_sum = float('-inf')
    sum = 0
    for x in A:
        sum = max(x, x + sum)
        best_sum = max(best_sum, sum)
    return best_sum

import numpy as np

def max_adj_sum_sub(m):
    assert m.shape[0] == m.shape[1]
    N = m.shape[0]
    best_sum = float('-inf')
    for n in range(N):
        best_sum = max(best_sum, max_adj_sum(m[n]))
        best_sum = max(best_sum, max_adj_sum(m[:,n]))
    rm = np.flipud(m)
    for n in range(-N+1,N):
        best_sum = max(best_sum, max_adj_sum(m.diagonal(n)))
        best_sum = max(best_sum, max_adj_sum(rm.diagonal(n)))
    return best_sum

def make_m():
    N = 2000
    m = np.zeros(N * N, dtype='int')
    for k in range(1, 56):
        m[k - 1] = (100003 - 200003*k + 300007*k**3) % 1000000 - 500000
    for k in range(56, 4000001):
        m[k - 1] = (m[k - 24 - 1] + m[k - 55 - 1] + 1000000) % 1000000 - 500000
    m = m.reshape((N, N))
    return m
