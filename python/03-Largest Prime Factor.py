# megatheriumNinja
import Functions as functions, datetime

num = 600851475143

for i in range(round(num/2+1), -1, -1):
	if functions.is_factor(num, i) and functions.is_prime(i):
		print(i)
		break