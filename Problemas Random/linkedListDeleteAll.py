class Node(object):
	def __init__(self, Data, Next=None):
		self.data = Data
		self.next = Next

class LinkedList(object):
	def __init__(self):
		self.head = None
		self.tail = None

	def show(self):
		currentNode = self.head
		print 'list: '
		while (currentNode is not None):
			if (currentNode is self.head and currentNode is self.tail):
				print 'head/tail: ' + str(currentNode.data)
			if (currentNode is self.head and currentNode is not self.tail):
				print 'head: ' + str(currentNode.data) + '->'
			if (currentNode is not self.head and currentNode is self.tail):
				print 'tail: ' + str(currentNode.data)
			if (currentNode is not self.head and currentNode is not self.tail):
				print str(currentNode.data) + '->'
			currentNode = currentNode.next

	def append(self, data):
		newNode = Node(data)
		if (self.head is None):
			self.head = newNode
			self.tail = newNode
		else:
			self.tail.next = newNode
			self.tail = newNode

	def deleteElem(self, data):
		currentNode = self.head
		while (currentNode is not None):
			if (currentNode is self.head and currentNode.data == data):
				self.head = currentNode.next
			else:
				if (currentNode.next.data == data):
					iteratingNode = currentNode.next
					while (iteratingNode is not None and iteratingNode.data == data):
						iteratingNode = iteratingNode.next

					if (iteratingNode is None):
						self.tail = currentNode
						currentNode.next = None
					else:
						currentNode.next = iteratingNode

			currentNode = currentNode.next
			if (currentNode is self.tail):
				currentNode = None





myList = LinkedList()
myList.append(7)
myList.append(8)
myList.append(8)
myList.append(6)
myList.append(8)

myList.deleteElem(8)
myList.show()














