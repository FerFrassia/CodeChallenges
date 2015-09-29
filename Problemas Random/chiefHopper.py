def energyRequired(li):
	if (len(li) < 2):
		if (len(li) == 1):
			return li[0]
		else:
			return 0
	else:
		i = len(li)-2
		energy = 0
		while (i >= 0):
			energy = energy + li[i+1] - li[i]
			i -= 1
		energy = energy + li[0]
		return energy

print energyRequired([3, 4, 3, 2, 4])