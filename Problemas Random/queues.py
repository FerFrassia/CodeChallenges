import Queue
q1 = Queue.Queue()
q2 = Queue.LifoQueue()
q3 = Queue.PriorityQueue()

def fifoQueue(q, intList):
	for val in intList:
		q.put(val)

def lifoQueue(q, intList):
	for val in intList:
		q.put(val)

def myPriorityQueue(q, intList):
	for val in intList:
		q.put(val)

def showQueue(q):
	while not q.empty():
		print q.get()


fifoQueue(q1, [0, 1, 2, 3])
print 'fifoQueue: '
showQueue(q1)

print ''

print 'lifoQueue: '
lifoQueue(q2, [0, 1, 2, 3])
showQueue(q2)

print ''

print 'PriorityQueue: '
myPriorityQueue(q3, [3, 1, 0, 3])
showQueue(q3)
