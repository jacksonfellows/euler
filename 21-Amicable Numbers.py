from math import sqrt

def d(num):
	s = 0
	num = float(num)
	for i in range(2, int(sqrt(num))):
		div = num / i
		if round(div) == div:
			s += i + div
	s = int(s) + 1
	return s

amicables = []
for i in range(1, 10001):
	if i in amicables:
		continue
	div_sum = d(i)
	if div_sum != i and d(div_sum) == i:
		amicables.append(i)
		amicables.append(div_sum)

print(sum(amicables))