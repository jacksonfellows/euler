from functools import lru_cache

@lru_cache(None)
def m(k):
    if k == 1:
        return (frozenset(),)
    mins = []
    min_len = float('inf')
    for i in range(1,k//2+1):
        for a in m(i):
            for b in m(k-i):
                x = a | b
                len_x = len(x)
                if len_x < min_len:
                    min_len = len_x
                    mins = [x]
                elif len_x == min_len:
                    mins.append(x)
    return tuple(frozenset((k,)) | min_ for min_ in mins)

def p122():
    return sum(len(m(k)[0]) for k in range(1,201))

print(p122())
