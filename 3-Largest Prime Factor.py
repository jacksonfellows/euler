# megatheriumNinja
import Functions as functions

num = 600851475143

factors = functions.factors(num)
prime_factors = []
for i in factors:
	if functions.is_prime(i):
		prime_factors.append(i)
largest_prime_factor = functions.largest(prime_factors)

print(largest_prime_factor)