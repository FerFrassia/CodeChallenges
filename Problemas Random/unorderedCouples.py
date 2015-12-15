def unorderedCouples(l, lower, upper):
	if lower == upper:
		return 0
	else:
		middle = lower + (upper-lower)/2

		leftCouples = unorderedCouples(l, lower, middle)
		rightCouples = unorderedCouples(l, middle+1, upper)

		couplesCrossing = 0
		i = lower
		j = middle+1

		while i < middle+1:
			while j <= upper and l[i] > l[j]:
				j += 1

			couplesCrossing += j - (middle+1)
			i += 1

		return leftCouples + rightCouples + couplesCrossing


print unorderedCouples([21, 20], 0, 1) 