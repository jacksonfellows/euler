def xor_with_key(key, encrypted):
    decrypted = []
    for i in range(len(encrypted)):
        decrypted.append(encrypted[i] ^ key[i % len(key)])
    return decrypted

def find_freqs(text):
    freqs = {}
    tot = 0
    for c in text:
        tot += 1
        if c in freqs:
            freqs[c] += 1
        else:
            freqs[c] = 1
    for k,v in freqs.items():
        freqs[k] = v / tot
    return freqs

def comp_freqs(standard, text):
    off = 0
    for k,v in text.items():
        if k in standard:
            off += abs(standard[k] - v)
        else:
            off += v
    for k,v in standard.items():
        if k not in text:
            off += v
    return off

with open('../pride_and_prejudice.txt') as sample:
    en_freqs = find_freqs(sample.read())

with open('../p059_cipher.txt') as encrypted_file:
    code = list(map(int, encrypted_file.read().split(',')))

letters = range(ord('a'), ord('z')+1)
min_score = None
message = None
for a in letters:
    for b in letters:
        for c in letters:
            key = (a,b,c)
            decrypted = ''.join(map(chr, xor_with_key(key, code)))
            score = comp_freqs(en_freqs, find_freqs(decrypted))
            if min_score == None or score < min_score:
                min_score = score
                message = decrypted

print('decrypted the message:')
print(message)
print()
print('the sum of the ASCII values is: %d' % sum(map(ord,list(message))))
