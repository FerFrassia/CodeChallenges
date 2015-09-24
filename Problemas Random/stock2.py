def bestProfit(stocks):
	if (len(stocks) < 2):
		return 'no profit possible'
	else:
		minStock = stocks[0]
		profit = stocks[1] - minStock
		i = 1
		while (i < len(stocks)):
			if (stocks[i] - minStock > profit):
				profit = stocks[i] - minStock
			if (stocks[i] < minStock):
				minStock = stocks[i]
			i += 1
		return profit

print bestProfit([-1, -3, 5, 6, -20, 30])