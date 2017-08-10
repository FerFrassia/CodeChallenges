class Node(object):
	def __init__(self, Data, Prev, Next):
		self.data = Data
		self.prev = Prev
		self.next = Next

class DoubleList(object):
	head = None
	tail = None
	length = 0

	def show(self):
		currentNode = self.head
		while (currentNode is not None):
			arrow = ''
			if (currentNode is not self.tail):
				arrow = '<->'
			print currentNode.data, arrow

			currentNode = currentNode.next

	def append(self, data):
		newNode = Node(data, None, None)
		if (self.tail is None):
			self.head = newNode
			self.tail = newNode
		else:
			self.tail.next = newNode
			newNode.prev = self.tail
			self.tail = newNode
		self.length += 1

	def appendAtFront(self,data):
		newNode = Node(data, None, None)
		if (self.head is None):
			self.head = newNode
			self.tail = newNode
		else:
			self.head.prev = newNode
			newNode.next = self.head
			self.head = newNode
		self.length += 1

	def delete(self, data):
		currentNode = self.head
		while (currentNode.data != data):
			currentNode = currentNode.next

		if (currentNode is self.head):
			if (currentNode is self.tail):
				self.tail = None
			else:
				currentNode.next.prev = None
			self.head = currentNode.next
		else:
			if (currentNode is not self.tail):
				currentNode.next.prev = currentNode.prev
			else:
				self.tail = currentNode.prev
			currentNode.prev.next = currentNode.next
		self.length -= 1


def mySum(a, b):
	if (a.length < b.length):
		mySum(b, a)
	else:
		currentNodeA = a.head
		currentNodeB = b.head
		resultList = DoubleList()
		carry = 0
		while (currentNodeA is not None):
			if (currentNodeB is not None):
				addedNumber = currentNodeA.data + currentNodeB.data + carry
				if (addedNumber >= 10):
					splitNumber = [int(i) for i in str(addedNumber)]
					carry = splitNumber[0]
					addedNumber = splitNumber[1]
				else:
					carry = 0

				resultList.append(addedNumber)
				currentNodeA = currentNodeA.next
				currentNodeB = currentNodeB.next
			else:
				resultList.append(currentNodeA.data)
				currentNodeA = currentNodeA.next

		resultList.show()

resultSum = DoubleList()
def reverseSum(a, b, nodeA, nodeB):
	if (nodeA is a.tail and nodeB is b.tail):
		addedNumber = nodeA.data + nodeB.data
		carry = 0
		if (addedNumber >= 10):
			splitNumber = [int(i) for i in str(addedNumber)]
			carry = splitNumber[0]
			addedNumber = splitNumber[1]
		resultSum.appendAtFront(addedNumber)
		return carry
	else:
		addedNumber = nodeA.data + nodeB.data + reverseSum(a, b, nodeA.next, nodeB.next)
		carry = 0
		if (addedNumber >= 10):
			splitNumber = [int(i) for i in str(addedNumber)]
			carry = splitNumber[0]
			addedNumber = splitNumber[1]
		resultSum.appendAtFront(addedNumber)
		return carry

def reverseTotalSum(a, b, nodeA, nodeB):
	if (a. length < b.length):
		reverseTotalSum(b, a, nodeB, nodeA)
	
	elif (a.length == b.length):
		return reverseSum(a, b, nodeA, nodeB)

	else:
		carry = 0
		print 'iterating'
		print 'nodeA data: ', nodeA.data
		adding = nodeA.data
		nextNodeA = nodeA.next
		a.delete(nodeA.data)
		addedNumber = adding + reverseTotalSum(a, b, nextNodeA, nodeB)
		if (addedNumber >= 10):
			splitNumber = [int(i) for i in str(addedNumber)]
			carry = splitNumber[0]
			addedNumber = splitNumber[1]
		resultSum.appendAtFront(addedNumber)
		return carry

def addingFirstCarry(a, b, nodeA, nodeB):
	carry = reverseTotalSum(a, b, nodeA, nodeB)
	if (carry != 0):
		resultSum.appendAtFront(carry)

	



# a = DoubleList()
# a.append(7)
# a.append(1)
# a.append(6)
# print 'list A: '
# a.show()

# b = DoubleList()
# b.appendAtFront(2)
# b.appendAtFront(9)
# b.appendAtFront(5)
# print ''
# print 'list B: '
# b.show()

# print ''
# print 'sum: ' 
# mySum(a, b)

a = DoubleList()
a.append(9)
a.append(9)
a.append(9)
#a.append(0)
#a.append(0)
print 'list A: '
a.show()

b = DoubleList()
b.append(9)
b.append(9)
b.append(9)
print ''
print 'list B: '
b.show()

print ''
print 'reverse sum: '
addingFirstCarry(a, b, a.head, b.head)
resultSum.show()














