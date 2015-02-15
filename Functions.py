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
	if i != 1 and i != 0 and num%i == 0:
		return True
	else:
		return False

def is_prime(num):	
	for i in range(round(num/2+1), -1, -1):
		if is_factor(num, i):
			return False
	return True