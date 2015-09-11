def eval (s):
	if s[0] != '(':
		return int(s)
	else:
		if s[1] == '(':
			parentesisCount = 1
			index = 2
			while parentesisCount > 0:
				if s[index] == '(':
					parentesisCount = parentesisCount + 1
				elif s[index] == ')':
					parentesisCount = parentesisCount - 1
				index = index + 1
			if s[index] == '+':
				return eval(s[1:index]) + eval(s[index + 1:-1])
			else:
				return eval(s[1:index]) * eval(s[index + 1:-1])
		else:
			index = 2
			while s[index] != '+' and s[index] != '*':
				index = index + 1
			if s[index] == '+':
				return int(s[1:index]) + eval(s[index + 1:-1])
			else:
				return int(s[1:index]) * eval(s[index + 1:-1])

sarasa = raw_input('Enter calculation: ')
print eval(sarasa)




# S = NUM | (EXP + EXP) | (EXP * EXP) 