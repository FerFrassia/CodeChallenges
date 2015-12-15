class Node(object):
	def __init__(self, Data, Next):
		self.data = Data
		self.next = Next

class SingleList(object):
	def __init__(self):
		self.head = None
		self.tail = None

	def show(self):
		currentNode = self.head
		while (currentNode is not None):
			print currentNode.data
			currentNode = currentNode.next

	def append(self, data):
		newNode = Node(data, None)
		if (self.head is None):
			self.head = newNode
		else:
			self.tail.next = newNode
		self.tail = newNode

	def appendFront(self, data):
		newNode = Node(data, None)
		if (self.head is not None):
			newNode.next = self.head
		else:
			self.tail = newNode
		self.head = newNode

		return newNode

	def reverseSubList(self, i, j):
		print 'indexes: ' + str(i) + ', ' + str(j)
		reversedList = SingleList()
		currentNode = self.head
		nodeIndex = 0
		while (nodeIndex < i):
			currentNode = currentNode.next
			nodeIndex += 1
		stopData = currentNode.data
		while (nodeIndex <= j):
			reversedList.appendFront(currentNode.data)
			currentNode = currentNode.next
			nodeIndex += 1
		while (currentNode is not None):
			reversedList.append(currentNode.data)
			currentNode = currentNode.next

		currentReversedNode = reversedList.appendFront(self.head.data)
		currentNode = self.head.next

		while (currentNode.data != stopData):
			newNode = Node(currentNode.data, None)
			newNode.next = currentReversedNode.next
			currentReversedNode.next = newNode
			currentReversedNode = newNode
			currentNode = currentNode.next

		print 'original: '
		self.show()
		print 'reversed: '
		reversedList.show()


l = SingleList()
l.append(1)
l.append(2)
l.append(3)
l.append(4)
l.append(5)
l.append(6)
l.reverseSubList(3, 5)




