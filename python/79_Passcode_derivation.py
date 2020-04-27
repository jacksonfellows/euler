with open('../p079_keylog.txt') as f:
    logins = [[int(d) for d in line.strip()] for line in f.readlines()]

def conflict(passcode, login):
    last_i = 0
    for x in login:
        try:
            i = passcode.index(x)
            if i < last_i:
                return True
            last_i = i
        except ValueError:
            pass
    return False

def combine(passcode, login):
    if conflict(passcode, login):
        pass
    elif len(login) == 0:
        yield passcode
    else:
        try:
            i = passcode.index(login[0])
            for pos in combine(passcode[i+1:], login[1:]):
                yield passcode[:i+1] + pos
        except ValueError:
            for i in range(len(passcode)+1):
                yield from combine(passcode[:i] + [login[0]] + passcode[i:], login[1:])

def combine_all(seqs):
    if len(seqs) == 0:
        pass
    elif len(seqs) == 1:
        yield seqs[0]
    else:
        for x in combine(seqs[0], seqs[1]):
            yield from combine_all([x] + seqs[2:])

def p79():
    return ''.join(map(str, list(combine_all(logins))[0]))
