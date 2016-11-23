file = open('13-Large Sum Input.txt', 'r')

ans = 0

for line in file:
	print('   %i' % int(line))
	ans += int(line)

print(' + ',end='')
for i in range(0,50):
	print('-',end='')

print('\n')

print(' %i' % ans)