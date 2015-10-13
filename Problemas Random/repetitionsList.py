def repetitions(l):
	if (len(l) == 0):
		return None
	elif (len(l) == 1):
		return l[0]
	else:
		mostRepeated = []
		highestRepetitions = 0
		i = 0
		startIndex = 0
		while (i < len(l)):
			if ((i != len(l)-1 and l[i+1] != l[i]) or (i == len(l)-1)):
				windowLength = i - startIndex + 1
				if (windowLength > highestRepetitions):
					highestRepetitions = windowLength
					mostRepeated = [l[i]]
				elif (windowLength == highestRepetitions):
					mostRepeated.append(l[i])
				startIndex = i+1
			i += 1
		return mostRepeated

print repetitions([1, 1, 1, 1, 2, 3, 3, 3, 3, 4, 5, 6, 7, 7, 7, 7, 8, 9, 9, 9, 9, 9, 9, 9, 9])