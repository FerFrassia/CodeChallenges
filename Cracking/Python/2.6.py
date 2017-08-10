class Node(object):
	def __init__(self, Data, Next):
		self.data = Data
		self.next = Next

class SingleList(object):
	head = None
	tail = None
	length = 0

	def show(self):
		currentNode = self.head
		nodesLeft = self.length
		while (nodesLeft != 0):
			if (currentNode is not self.tail):
				print currentNode.data, '->'
			else:
				print currentNode.data
			currentNode = currentNode.next
			nodesLeft -= 1

	def append(self, data):
		newNode = Node(data, None)
		if (self.head is None):
			self.head = newNode
		else:
			self.tail.next = newNode
		self.tail = newNode
		self.length += 1

	def appendLoop(self, data, nodeNumber):
		newNode = Node(data, None)
		if (self.length == 0):
			self.head = newNode
		else:
			self.tail.next = newNode
		self.length += 1
		newNode.next = self.nodeAtPos(nodeNumber)
		self.tail = newNode

	def nodeAtPos(self, nodeNumber):
		currentNumber = 0
		currentNode = self.head
		while (currentNumber != nodeNumber):
			currentNode = currentNode.next
			currentNumber += 1

		return currentNode

	def findLoopPos(self):
		if (self.length == 0 or (self.length == 1 and self.head.next is None)):
			return -1
		else:
			if (self.length == 1 and self.head.next is self.head):
				return 0
			else:
				turtle = self.head
				rabbit = self.head.next.next
				
				while (turtle is not None and rabbit is not None and turtle is not rabbit):
					turtle = turtle.next
					if (rabbit.next is not None):
						rabbit = rabbit.next.next
					else:
						rabbit = None

				if (rabbit is None):
					return -1
				else:
					#rabbit and turtle have met
					#I find the length of the loop
					loopLength = 1
					turtle = turtle.next
					while (rabbit is not turtle):
						turtle = turtle.next
						loopLength += 1

					return self.length - loopLength



s = SingleList()
s.append(5)
s.append(10)
s.appendLoop(8, 1)
s.show()
print ''
print '8.next: ', s.nodeAtPos(2).next.data
print ''
print 'loop pos: ', s.findLoopPos()

