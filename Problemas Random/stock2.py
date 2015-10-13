# returns best profit
def stock(l):
	bestMin = 0
	bestProfit = 0
	i = 0
	while (i < len(l)):
		if (l[i] < l[bestMin]):
			bestMin = i
		if (l[i] - l[bestMin] > bestProfit):
			bestProfit = l[i] - l[bestMin]
		i += 1

	return bestProfit

#returns buying and selling indexes
def stockIndex(l):
	bestMin = 0
	bestMax = 0
	i = 0
	while (i < len(l)):
		if (l[i] < l[bestMin]):
			bestMin = i
		if (l[i]-l[bestMin] > l[bestMax]-l[bestMin]):
			bestMax = i
		i += 1

	if (bestMin >= bestMax):
		return (0, 0)
	else:
		return (bestMin, bestMax)

print 'max profit: ' + str(stock([10, 9, 8, 7, 6, 5]))
print 'max indexes: ' + str(stockIndex([10, 9, 8, 7, 6, 5]))