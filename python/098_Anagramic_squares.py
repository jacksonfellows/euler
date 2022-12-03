words = eval('(' + open('../p042_words.txt').read() + ')')

def find_anagrams(word_list):
    word_map = {}
    for w in word_list:
        word_map[tuple(sorted(w))] = word_map.get(tuple(sorted(w)), tuple()) + (w,)
    return [v for v in word_map.values() if len(v) > 1]

from itertools import *

def make_number(word, mapping):
    n = 0
    for letter in word:
        n = 10 * n + mapping[letter]
    return n

from math import *

def is_square(n):
    s = int(sqrt(n))
    return s * s == n

def is_pair(a, b):
    print(f'is_pair({a}, {b})')
    letters = set(a)
    for assignment in permutations(range(10), len(letters)):
        mapping = {l: n for l, n in zip(letters, assignment)}
        if mapping[a[0]] == 0 or mapping[b[0]] == 0:
            continue
        x = make_number(a, mapping)
        y = make_number(b, mapping)
        if is_square(x) and is_square(y):
            return max(x, y)
    return 0

def find_max(pairs):
    return max(map(lambda p: is_pair(p[0], p[1]), pairs))

def get_pairs(anagrams):
    pairs = []
    for s in anagrams:
        pairs.extend(combinations(s, 2))
    return pairs
