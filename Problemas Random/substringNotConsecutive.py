def substringNotConsecutive(l, sub):
	l = list(l)
	sub = list(sub)
	i = 0
	j = 0
	while (i < len(l) and j < len(sub)):
		if (l[i] == sub[j]):
			j += 1
		i += 1

	if (j == len(sub)):
		return True
	else:
		return False

print substringNotConsecutive('abretesesamo', 'om')