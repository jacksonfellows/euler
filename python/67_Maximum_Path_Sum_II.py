file = open('67-Maximum Path Sum II Input.txt', 'r')

l = [[int(i) for i in line.split(' ')] for line in file]

def max_path_sum(l):
	for i in range(len(l)-1, 0, -1):
		for j in range(len(l[i])-1):
			l[i-1][j] += max(l[i][j], l[i][j+1])

	return l[0][0]

print(max_path_sum(l))