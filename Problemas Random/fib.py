def fib(n):
	if (n == 0):
		return 0
	elif (n == 1):
		return 1
	else:
		fib_prev_prev = 0
		fib_prev = 1
		i = 2
		while (i <= n):
			val = fib_prev + fib_prev_prev
			fib_prev_prev = fib_prev
			fib_prev = val
			i += 1
		return fib_prev

for i in range(20):
	print fib(i)