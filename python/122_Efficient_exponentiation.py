ms = {1:[set()]}

def fill_row(k):
    mins = []
    min_len = float('inf')
    for i in range(1,k//2+1):
        for a in ms[i]:
            for b in ms[k-i]:
                x = a | b
                len_x = len(x)
                if len_x < min_len:
                    min_len = len_x
                    x.add(k)
                    mins = [x]
                elif len_x == min_len:
                    x.add(k)
                    mins.append(x)
    ms[k] = mins
    return 1 + min_len

def p122():
    s = 0
    for k in range(2,201):
        s += fill_row(k)
    return s

print(p122())
