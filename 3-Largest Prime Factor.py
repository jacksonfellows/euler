# megatheriumNinja
import Functions as functions, datetime

start_time = datetime.datetime.now()

num = 600851475143

for i in range(round(num/2+1), -1, -1):
	if functions.is_factor(num, i) and functions.is_prime(i):
		print(i)
		break

end_time = datetime.datetime.now()

total_time = end_time - start_time

print("It took " + str(total_time))