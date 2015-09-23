import Queue
littleQueueSize = 5
bigStack = []

class littleStack(object):
	def __init__(self, Stack, Next):
		self.stack = Stack
		self.next = Next

class bigStack(object):
	top = None

	def pushBig(self, data):
		if (self.top is None or self.top.stack.full()):
			stack = Queue.Queue(littleQueueSize)
			stack.put(data)
			newLittleStack = littleStack(stack, self.top)
			self.top = newLittleStack
		else:
			self.top.stack.put(data)

	def popBig(self):
		if (self.top is None or (self.top.stack.empty() and self.top.next is None)):
			self.top = None
			return
		else:
			topStack = self.top.stack
			if (topStack.empty()):
				self.top = self.top.next
				print 'change of stack: '
			topStack = self.top.stack
			return topStack.get()

	def showBig(self):
		print 'big stack: '
		while (self.top is not None):
			print self.popBig()

	def popAt(self, destinationStackIndex):
		currentLittleStack = self.top
		currentStackIndex = 0
		while (currentStackIndex < destinationStackIndex):
			currentLittleStack = currentLittleStack.next
			currentStackIndex += 1
		return currentLittleStack.stack.get()


def showLittle(q):
	while not q.empty():
		print q.get()

big = bigStack()
big.pushBig(5)
big.pushBig(6)
big.pushBig(7)
big.pushBig(8)
big.pushBig(9)
big.pushBig(10)
big.pushBig(20)
big.pushBig(30)
big.pushBig(40)
big.pushBig(50)
big.pushBig(100)
#big.showBig()
print 'pop at 1: ', big.popAt(1)
print ''
big.showBig()


