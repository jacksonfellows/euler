from operator import add, sub, mul, truediv
from itertools import product

def sorted_k_partitions(seq, k):
    n = len(seq)
    groups = []

    def generate_partitions(i):
        if i >= n:
            yield list(map(tuple, groups))
        else:
            if n - i > k - len(groups):
                for group in groups:
                    group.append(seq[i])
                    yield from generate_partitions(i + 1)
                    group.pop()

            if len(groups) < k:
                groups.append([seq[i]])
                yield from generate_partitions(i + 1)
                groups.pop()

    result = generate_partitions(0)

    return result

def eval_exprs(digits):
    if len(digits) == 1:
        yield digits[0]
    else:
        for op in [add, sub, mul, truediv]:
            for left, right in sorted_k_partitions(digits, 2):
                for l, r in product(eval_exprs(left), eval_exprs(right)):
                    try: yield op(l, r)
                    except: pass
                    if op in [sub, truediv]:
                        try: yield op(r, l)
                        except: pass

def n_conseq_nat_targets(digits):
    targets = set()
    for x in eval_exprs(digits):
        i = int(x)
        if x > 0 and x == i:
            targets.add(i)

    targets = sorted(list(targets))

    try:
        return next(targets[i-1] for i,x in enumerate(targets) if i > 0 and x != targets[i-1] + 1)
    except:
        return targets[-1]

def p93():
    max_digits = None
    max_l = 0
    for a in range(7):
        for b in range(a+1,8):
            for c in range(b+1,9):
                for d in range(c+1,10):
                    l = n_conseq_nat_targets([a,b,c,d])
                    if l > max_l:
                        max_digits = [a,b,c,d]
                        max_l = l
    return ''.join(str(digit) for digit in max_digits)
