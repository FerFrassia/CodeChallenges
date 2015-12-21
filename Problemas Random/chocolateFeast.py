def chocoFeast(n, c, m):
	eaten = n / c
	wrappersLeft = eaten
	while wrappersLeft >= m:
		eaten += 1
		wrappersLeft -= m
		wrappersLeft += 1

	return eaten

print chocoFeast(6, 2, 2)


# Problem Statement

# Little Bob loves chocolate, and he goes to a store with $N in his pocket. 
# The price of each chocolate is $C. The store offers a discount: for every M wrappers he gives to the store, 
# he gets one chocolate for free. How many chocolates does Bob get to eat?