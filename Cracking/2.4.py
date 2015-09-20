class Node(object):
	def __init__(self, Data, Prev, Next):
		self.data = Data
		self.next = Next
		self.prev = Prev

class DoubleList(object):
	head = None
	tail = None

	def show(self):
		currentNode = self.head
		while (currentNode is not None):
			if (currentNode is self.tail):
				print currentNode.data
			else:
				print currentNode.data, '<->'
			currentNode = currentNode.next

	def appendAtLast(self, data):
		newNode = Node(data, None, None)
		if (self.tail is None):
			self.head = newNode
			self.tail = newNode
		else:
			self.tail.next = newNode
			newNode.prev = self.tail
			self.tail = newNode

	def appendAtBeginning(self, data):
		newNode = Node(data, None, None)
		if (self.head is None):
			self.head = newNode
			self.tail = newNode
		else:
			self.head.prev = newNode
			newNode.next = self.head
			self.head = newNode

	def delete(self, data):
		currentNode = self.head
		while (currentNode.data != data):
			currentNode = currentNode.next

		if (self.head is currentNode):
			if (self.tail is currentNode):
				self.head = None
				self.tail = None
			else:
				currentNode.next.prev = None
				self.head = currentNode.next
		else:
			if (self.tail is currentNode):
				currentNode.prev.next = None
				self.tail = currentNode.prev
			else:
				currentNode.prev.next = currentNode.next
				currentNode.next.prev = currentNode.prev

	def arrangeByX(self, data):
	 	currentNode = self.head
	 	newList = DoubleList()

	 	while (currentNode.data != data):
	 		currentNode = currentNode.next

	 	newList.appendAtBeginning(currentNode.data)
	 	currentNode = self.head
	 	ignoreData = True
	 	while (currentNode is not None):
	 		if (currentNode.data < data):
	 			newList.appendAtBeginning(currentNode.data)
	 		else:
	 			if (currentNode.data == data):
	 				if (ignoreData):
	 					ignoreData = False
	 				else:
	 					newList.appendAtLast(currentNode.data)
	 			else:
	 				newList.appendAtLast(currentNode.data)

 			currentNode = currentNode.next

	 	newList.show()


s = DoubleList()
s.appendAtLast(5)
s.appendAtLast(10)
s.appendAtLast(20)
s.appendAtLast(1)
s.appendAtLast(2)
s.appendAtLast(3)
s.appendAtLast(4)
s.appendAtLast(5)
s.show()
print ''
s.arrangeByX(5)





















