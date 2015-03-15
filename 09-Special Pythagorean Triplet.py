import Functions as functions, datetime

start_time = datetime.datetime.now()

for a in range(1, 1000):
	for b in range(a, 1000):
		for c in range(b, 1000):
			if a + b + c == 1000 and a**2 + b**2 == c**2:
				print(a * b * c)

end_time = datetime.datetime.now()

total_time = end_time - start_time

print("It took " + str(total_time))