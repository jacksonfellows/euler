d = 1001
s = 1
for x in range(2, d//2 + 2):
	s += 16*x**2 - 28*x + 16
print(s)