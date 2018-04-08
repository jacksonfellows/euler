from math import sqrt

def sum_of_divisors(n):
	sr = int(sqrt(n) + 1)
	s = 1
	for i in range(2, sr):
		x = n / i
		if round(x) == x:
			s += i
			s += x
	return int(s)

def is_abundant(n):
	return sum_of_divisors(n) > n

abundants = []
for i in range(1, 28123):
	if is_abundant(i):
		abundants.append(i)
print('found abundant nums')

sums = []
for i in abundants:
	for j in abundants:
		if j != i:
			sums.append(i + j)
print('found abundant sums')

is_sum = [False] * (28123 + 2)
for i in sums:
	if i < len(is_sum):
		is_sum[i] = True
print('marked sums')

final_sum = 0
for i in range(len(is_sum)):
	if not is_sum[i]:
		print(i)
		final_sum += i
print('got final total')

print(final_sum)