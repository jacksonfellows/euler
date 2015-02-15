#megatheriumNinja
import Functions as functions

list = []

for i in range(1000, -1, -1):
	for j in range(1000, -1, -1):
		num = i * j
		if str(num) == str(num)[::-1]:
			list.append(num)

list.sort()
print(list[-1])
