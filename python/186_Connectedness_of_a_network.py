import functools

@functools.cache
def S(k):
    assert(k > 0)
    if 1 <= k <= 55:
        return (100003 - 200003*k + 300007*k**3) % 1000000
    return (S(k - 24) + S(k - 55)) % 1000000

# Prime Minister: S(3_681_162) == 524287

prime_minister = 524287

import collections

def expand_pm_friends(G, pm_friends, x):
    edge_set = G[x] - pm_friends
    new_edge_set = set()
    while len(edge_set) > 0:
        for e in edge_set:
            pm_friends.add(e)
            new_edge_set |= G[e] - pm_friends
        edge_set, new_edge_set = new_edge_set, set()

def p186():
    G = collections.defaultdict(lambda: set())
    pm_friends = set([prime_minister])
    n = 1
    n_successful_calls = 0
    while True:
        if n % 100000 == 0:
            print(n, n_successful_calls, len(G))
        caller, called = S(2*n - 1), S(2*n)
        if caller != called:
            n_successful_calls += 1
            G[caller].add(called)
            G[called].add(caller)
            if caller in pm_friends and called in pm_friends:
                pass
            elif caller in pm_friends:
                expand_pm_friends(G, pm_friends, caller)
            elif called in pm_friends:
                expand_pm_friends(G, pm_friends, called)
            if caller in pm_friends:
                if len(pm_friends) >= 990000:
                    print(len(pm_friends), len(G), n, n_successful_calls)
                    break
        n += 1
    return n_successful_calls
