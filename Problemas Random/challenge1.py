# Devise a function that takes an input 'n' (integer) and returns a string that is the
# decimal representation of the number grouped by commas after every 3 digits. Do not
# solve the task using a built-in formatting function that can accomplish the whole
# task on its own.

# Assume: 0 <= n < 1000000000

# 1 -> "1"
# 10 -> "10"
# 100 -> "100"
# 1000 -> "1,000"
# 10000 -> "10,000"
# 100000 -> "100,000"
# 1000000 -> "1,000,000"
# 35235235 -> "35,235,235"
# 999999999 -> "999,999,999"


def parseTo3Digits(n):
	l = list(str(n))
	i = len(l) - 1
	returnString = ''
	counter = 0
	while (i >= 0):
		if (counter != 3):
			returnString = l[i] + returnString
			counter += 1
		else:
			returnString = l[i] + ',' + returnString
			counter = 1
		i -= 1
	return returnString

print parseTo3Digits(1)
print parseTo3Digits(10)
print parseTo3Digits(100)
print parseTo3Digits(1000)
print parseTo3Digits(10000)
print parseTo3Digits(100000)
print parseTo3Digits(1000000)
print parseTo3Digits(35235235)
print parseTo3Digits(999999999)
