import functools

@functools.cache
def expected(envelope):
    if envelope == (5,):
        return 0
    e = 1 if len(envelope) == 1 else 0
    for i,paper in enumerate(envelope):
        envelope_ = envelope[:i] + envelope[i+1:] + tuple(range(paper + 1, 6))
        e += expected(tuple(sorted(envelope_))) / len(envelope)
    return e

def p151():
    return round(expected((2,3,4,5)), 6)
