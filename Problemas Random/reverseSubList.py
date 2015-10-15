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
		reversedList = SingleList()
		currentNode = self.head
		nodeIndex = 0
		while (nodeIndex < i):
			currentNode = currentNode.next
			nodeIndex += 1
		while (nodeIndex <= j):
			reversedList.appendFront(currentNode.data)
			currentNode = currentNode.next
			nodeIndex += 1
		while (currentNode is not None):
			reversedList.append(currentNode.data)
			currentNode = currentNode.next

		stopData = reversedList.head.data
		curentReversedNode = reversedList.appendFront(self.head.data)
		currentNode = self.head.next

		while (currentReversedNode.next.data != stopData):
			



		reversedList.show()





l = SingleList()
l.append(1)
l.append(2)
l.append(3)
l.append(4)
l.reverseSubList(1, 2)




