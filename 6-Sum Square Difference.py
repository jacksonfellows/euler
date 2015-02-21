#megatheriumNinja
import Functions as functions, datetime

start_time = datetime.datetime.now()

num1 = 0
num2 = 0

for i in range(1, 101):
	num1 += i

num1 = num1 ** 2

for i in range(1, 101):
	num2 += i ** 2

print(num1 - num2)

end_time = datetime.datetime.now()

total_time = end_time - start_time

print("It took " + str(total_time))