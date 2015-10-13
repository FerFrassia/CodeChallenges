# complexity = O(n**2)
def largestIncreasing(l):
	maxIncreasing = []
	i = 0
	while (i < len(l)):
		j = i
		currentIncreasing = []
		currentStart = j
		while (j < len(l)):
			if (l[j] >= l[currentStart]):
				currentIncreasing.append(l[j])
				currentStart = j
			j += 1
		if (len(currentIncreasing) > len(maxIncreasing)):
			maxIncreasing = currentIncreasing
		i += 1

	return maxIncreasing

print largestIncreasing([1, 2, 1, 3, 2, 3, 4])

#complexity = O(n logn)
# def largestIncreasingDP(l):


