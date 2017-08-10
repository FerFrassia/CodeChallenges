#input: array of n x n
#outpit: same array but rotated
def rotateImage(a):
	newMatrix = [[]] * len(a)
	i = 0
	while (i < len(a)):
		i2 = 0
		j = 0
		while (j < len(a[i])):
			newMatrix[i2] =  [a[i][j]] + newMatrix[i2]
			j = j+1
			i2 = i2+1
		i = i+1
	return newMatrix

print rotateImage([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])




# [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]

#  1  2  3  4  5
#  6  7  8  9 10
# 11 12 13 14 15
# 16 17 18 19 20
# 21 22 23 24 25

# 21 16 11  6  1
# 22 17 12  7  2
# 23 18 13  8  3
# 24 19 14  9  4
# 25 20 15 10  5

# [[21, 16, 11, 6, 1], [22, 17, 12, 7, 2], [23, 18, 13, 8, 3], [24, 19, 14, 9, 4], [25, 20, 15, 10, 5]]