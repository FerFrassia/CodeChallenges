import Queue
myStack = Queue.Queue()

class Node(object):
	def __init__(self, Data, Min):
		self.data = Data
		self.min = Min

def push(q, val):
	newNode = Node(val, None)
	if (q.empty()):
		newNode.min = val
	else:
		newNode.min = min(val, peek(q).min)
	print 'pushing', val, newNode.min
	q.put(newNode)

def peek(q):
	returnNode = q.get()
	print 'returnNode: ', returnNode.data
	q.put(returnNode)
	return returnNode

def showQueue(q):
	while not q.empty():
		print q.get().data

push(myStack, 5)
push(myStack, 6)
peek(myStack)
peek(myStack)
peek(myStack)
peek(myStack)
peek(myStack)
peek(myStack)
# push(myStack, 3)
# push(myStack, 7)
#print showQueue(myStack)
#peek(myStack).data, peek(myStack).min
# push(myStack, 7)
# print 'min when pushing 7: ', peek(myStack).min
# print 'queue: '
# print showQueue(myStack)