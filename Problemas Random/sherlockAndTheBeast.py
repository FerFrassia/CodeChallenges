def decentNumber(n):
		if n % 3 == 0:
			return int(''.join(['5'] * n))
		elif n % 5 == 0:
			return int(''.join(['3'] * n))
		elif checkDecent(n) != None:
			myDic = checkDecent(n)
			l3 = ''.join(['3'] * 5*myDic['multiply5'])
			l5 = ''.join(['5'] * 3*myDic['multiply3'])
			return int(l5+l3)
		else:
			return -1

def checkDecent(n):
	toReturn = None
	for i in xrange(n):
		if (n - 5*i) % 3 == 0 and 5*i <= n:
			toReturn = i
	
	if toReturn != None:
		return {'multiply5':toReturn, 'multiply3':(n-5*toReturn)/3}
	else:
		return None

print decentNumber(1)
print decentNumber(3)
print decentNumber(5)
print decentNumber(11)

# Problem Statement

# Sherlock Holmes suspects his archenemy, Professor Moriarty, is once again plotting something diabolical. Sherlock's companion, Dr. Watson, suggests Moriarty may be responsible for MI6's recent issues with their supercomputer, The Beast.

# Shortly after resolving to investigate, Sherlock receives a note from Moriarty boasting about infecting The Beast with a virus; however, he also gives him a clue—a number, N. Sherlock determines the key to removing the virus is to find the largest Decent Number having N digits.

# A Decent Number has the following properties:

# Its digits can only be 3's and/or 5's.
# The number of 3's it contains is divisible by 5.
# The number of 5's it contains is divisible by 3.
# Moriarty's virus shows a clock counting down to The Beast's destruction, and time is running out fast. Your task is to help Sherlock find the key before The Beast is destroyed!