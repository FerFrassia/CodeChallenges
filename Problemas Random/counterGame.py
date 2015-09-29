def move(s):
	i = 1
	isPowerOfTwo = True
	while (i < len(s)-1):
		if (s[i] == '1'):
			isPowerOfTwo = False
		i += 1
	if (isPowerOfTwo):
		s = s[:-1]
	else:
		closePowerOfTwo = '0b1' + '0'*(len(s)-1)
		closePowerOfTwo = int(closePowerOfTwo, 2)
		sInt = int('0b'+s, 2)
		s = str(sInt - closePowerOfTwo)
	return int(s)


def winner(n):
	global turn
	if (n == 1):
		if (turn == 'Louise'):
			print 'Richard'
		else:
			print 'Louise'
	else:
		n = move(bin(n)[2:])
		if (turn == 'Louise'):
			turn = 'Richard'
		else:
			turn = 'Louise'
		winner(n)

turn = 'Louise'
winner(6)