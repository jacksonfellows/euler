#megatheriumNinja
import Functions as functions, datetime

start_time = datetime.datetime.now()

list = []

for i in range(1000, -1, -1):
	for j in range(1000, -1, -1):
		num = i * j
		if str(num) == str(num)[::-1]:
			list.append(num)

list.sort()
print(list[-1])

end_time  = datetime.datetime.now()

total_time = end_time - start_time

print("It took " + str(total_time))