# megatheriumNinja
def fibonacci(limit):
	num = 0
	seq = [1, 1]
	while num < limit:
		if num != 0: seq.append(num)
		num = seq[-1] + seq[-2]
	return seq

def return_evens(list):
	new_list = []
	for i in list:
		if i % 2 == 0:
			new_list.append(i)
	return new_list

def sum_up_list(list):
	value = 0
	for i in list:
		value += i
	return value

def multiples_under_limit(num, limit):
	total = 0
	i = 1
	product = 0

	while product < limit:
		total += product
		product = i * num
		i += 1
	return total

def is_factor(num, i):
	if i != 1 and i != 0 and num % i == 0:
		return True
	else:
		return False

def is_prime(num):	
	for i in range(round(num/2), -1, -1):
		if is_factor(num, i):
			return False
	return True

def nth_prime(num):
	primes = [2]
	i = 3

	while len(primes) < num:
		for prime in primes:
			if i % prime == 0:
				i += 1
				break
			elif prime > i / 2:
				primes.append(i)
				i += 1
				break

	return i - 1

def sum_of_primes_under(num):
	primes = [2]
	i = 3

	while primes[-1] < num:
		for prime in primes:
			if i % prime == 0:
				i += 1
				break
			elif prime > i / 2:
				primes.append(i)
				i += 1
				break


	del primes[-1]
	return sum_up_list(primes)

def find_vericals(l, length, slices):
	for i in range(0, length):
		l = []
		for j in slices:
			l.append(j[i])
		slices.append(l)

	return slices

def find_diagnols(l, length, slices):
	for i in range(0, length):
		l = []
		n = i
		for j in slices:
			if n == 20: break
			l.append(j[n])
			n += 1
		slices.append(l)

	for i in range(length-1, -1, -1):
		l = []
		n = i
		for j in slices:
			if n == -1: break
			l.append(j[n])
			n -= 1
		slices.append(l)

	return slices

def divisors(num):
	d = []
	for i in range(1, num+1):
		if num % i == 0:
			d.append(i)
	return(d)
