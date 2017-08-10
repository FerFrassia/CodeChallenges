#input: matrix, with ints
#output: list of positions where value is 0
def findCeros(a):
	ceros = [[], []]
	i = 0
	while (i < len(a)):
		j = 0
		while (j < len(a[i])):
			if (a[i][j] == 0):
				ceros[0].append(i)
				ceros[1].append(j)
			j = j+1
		i = i+1
	return ceros

print findCeros([[1, 2, 3], [5, 6, 0], [9, 5, 3, 1, 5, 4], [0], []])

# 1 2 3
# 5 6 0
# 9 5 3 1 5 4
# 0

# 0 2 0
# 0 0 0
# 0 5 0 1 5 4 
# 0

# [[0, 2, 0], [0, 0, 0], [0, 5, 0, 1, 5, 4], [0]]

# [[1, 3], [2, 0]]

def setCeros(a):
	ceros = findCeros(a)
	i = 0
	while (i < len(a)):
		if (i in ceros[0]):
			a[i] = [0] * len(a[i])
		else:
			j = 0
			while (j < len(a[i])):
				if (j in ceros[1]):
					a[i][j] = 0
				j = j+1
		i = i+1

	return a

print setCeros([[1, 2, 3], [5, 6, 0], [9, 5, 3, 1, 5, 4], [0], []])

