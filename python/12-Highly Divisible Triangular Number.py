import numpy as np # trying numpy out for solving these problems
from math import sqrt

def tri(n):
	a = np.arange(1,n+1,1)
	return(a.sum())

def divisors(num):
	d = []
	step = 2 if num%2 else 1
	for i in range(1, int(sqrt(num))+1, step):
		if num%i == 0 and i*i != num:
			d.append([i,num/i])
		elif i*i == num:
			d.append([i])

	return(sum(d,[]))

maximum = 100000

l = []

for i in range(1,maximum+1):
	tria = tri(i)
	num_divisors = len(divisors(tria))
	l.append([tria,num_divisors])
	if num_divisors > 500:
		break
print('the triangle number of %f has more than 500 divisors' % i)
print(l[i-1][0])