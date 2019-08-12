def units(n, a):
	w = ''

	if n == 1:
		if a == True:
			w += 'a'
		else:
			w += 'one'
	elif n == 2:
		w += 'two'
	elif n == 3:
		w += 'three'
	elif n == 4:
		w += 'four'
	elif n == 5:
		w += 'five'
	elif n == 6:
		w += 'six'
	elif n == 7:
		w += 'seven'
	elif n == 8:
		w += 'eight'
	elif n == 9:
		w += 'nine'

	return(w)

def tens(n):
	w = ''

	if n == 10:
		w += 'ten'
	elif n == 11:
		w += 'eleven'
	elif n == 12:
		w += 'twelve'
	elif 12 < n < 20:
		if n == 13:
			w += 'thir'
		elif n == 14:
			w += 'four'
		elif n == 15:
			w += 'fif'
		elif n == 16:
			w += 'six'
		elif n == 17:
			w += 'seven'
		elif n == 18:
			w += 'eigh'
		elif n == 19:
			w += 'nine'
		w += 'teen'
	elif n == 20:
		w += 'twenty'
	elif n == 30:
		w += 'thirty'
	elif n == 40:
		w += 'forty'
	elif n == 50:
		w += 'fifty'
	elif n == 60:
		w += 'sixty'
	elif n == 70:
		w += 'seventy'
	elif n == 80:
		w += 'eighty'
	elif n == 90:
		w += 'ninety'
	else:
		w += tens(int(str(n)[0]+'0'))
		w += units(int(str(n)[1]), a=False)

	return(w)

def hundreds(n):
	w = ''

	w += units(int(str(n)[0]),a=False)
	w += 'hundred'
	if str(n)[-2] == '0':
		w += 'and'
		w += units(int(str(n)[-1]), a=False)
	else:
		w += 'and'
		w += tens(int(str(n)[-2]+str(n)[-1]))

	if w[-3:] == 'and':
		w = w[:-3]

	if w == 'ahundred':
		w = 'onehundred'

	return(w)

def words(n):
	if len(str(n)) == 1:
		return(units(n, a=False))
	elif len(str(n)) == 2:
		return(tens(n))
	elif len(str(n)) == 3:
		return(hundreds(n))
	elif len(str(n)) == 4:
		return('onethousand')

count = 0

for i in range(1,1001):
	# print(words(i))
	# print(len(words(i)))
	count += len(words(i))

print('The number of letters used in all the numbers written out from 1 to 1000 is:')
print(count)
