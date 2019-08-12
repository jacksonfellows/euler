def paths(n):
	f1 = 1
	for i in range(1,n*2+1):
		f1 *= i
	f2 = 1
	for i in range(1,n+1):
		f2 *= i

	p = f1 // (f2**2)

	return(p)

print(paths(20))
