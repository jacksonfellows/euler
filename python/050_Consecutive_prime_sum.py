from erat import erat

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
