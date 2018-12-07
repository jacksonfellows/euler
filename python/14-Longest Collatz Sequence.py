import time
start_time = time.time()

def collatz(n):
	seq = []
	while n != 1:
		seq.append(n)
		if n%2 == 0:
			n = n/2
		else:
			n = 3*n+1
	seq.append(1)
	return(seq)

l = []

for i in range(1,1000000):
	l.append(len(collatz(i)))

longest = l.index(max(l))

print('The number with the longest collatz chain is %i' % (longest+1))
print('The chain is %i steps long' % len(collatz(longest+1)))
print('The chain is:')
print(collatz(longest+1))

print("--- %s seconds ---" % (time.time() - start_time))