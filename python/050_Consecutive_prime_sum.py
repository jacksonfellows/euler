def erat(lim):
    is_prime = [True] * (lim+1)
    is_prime[0] = False
    is_prime[1] = False

    primes = []

    i = 0
    while True:
        while i < lim+1 and not is_prime[i]: i += 1
        if i >= lim+1: break
        primes.append(i)
        for j in range(i*i, lim+1, i):
            is_prime[j] = False
        i += 1

    return primes, is_prime

lim = 1000000
primes, is_prime = erat(lim)

max_sum = None
max_len = 0

for i in range(len(primes)):
    for j in range(i+1,len(primes)):
        l = j - i
        s = sum(primes[i:j])
        if s > lim:
            break
        if is_prime[s] and l > max_len:
            max_len = l
            max_sum = s

print(max_len)
print(max_sum)
