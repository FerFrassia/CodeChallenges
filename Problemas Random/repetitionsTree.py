class Node(object):
	def __init__(self, Data, Left, Right, Father):
		self.data = Data
		self.left = Left
		self.right = Right
		self.father = Father

class BinaryTree(object):
	def __init__(self):
		self.root = None

	def add(self, data):
		node = Node(data, None, None, None)
		if (self.root is None):
			self.root = node
		else:
			currentNode = self.root
			while ((node.data >= currentNode.data and currentNode.right is not None) or (node.data < currentNode.data and currentNode.left is not None)):
				if (node.data < currentNode.data):
					currentNode = currentNode.left
				else:
					currentNode = currentNode.right

			if (node.data < currentNode.data):
				currentNode.left = node
			else:
				currentNode.right = node
			node.father = currentNode

	def show(self, node):
		if (node is not None):
			print '( ' + str(node.data),
			if (node.left is not None):
				print ', left: ' + str(node.left.data),
			if (node.right is not None):
				print ', right: ' + str(node.right.data),
			if (node.father is not None):
				print ', father: ' + str(node.father.data),
			print ')'
			self.show(node.left)
			self.show(node.right)

	mostRepeatedAll = None
	highestRepetition = 0
	def mostRepeated(self, node, currentVal, currentRepetition):
		if (node is not None):
			self.mostRepeated(node.left, currentVal, currentRepetition)
			if (node.data != currentVal):
				currentVal = node.data
				currentRepetition = 1
			else:
				currentRepetition += 1
				if (currentRepetition > self.highestRepetition):
					self.highestRepetition = currentRepetition
					self.mostRepeatedAll = currentVal
			self.mostRepeated(node.right, currentVal, currentRepetition)

	def lowestCommonAncestor(self, node, d1, d2):
		if (node is not None):
			if (node.data == d1 or node.data == d2):
				return node.data
			else:

				left = self.lowestCommonAncestor(node.left, d1, d2)
				right = self.lowestCommonAncestor(node.right, d1, d2)

				if (left is not None and right is not None):
					return node.data
				elif (left is not None and right is None):
					return left
				else:
					return right

	def biggestSum(self, node):
		if node is not None:
			if node.left is None and node.right is None:
				return (node.data, node.data)
			else:
				sumLeft = self.biggestSum(node.left)
				sumRight = self.biggestSum(node.right)

				maxSum = max(sumLeft[0], sumRight[0], sumLeft[1] + sumRight[1] + node.data)
				maxBranch = max(sumLeft[1] + node.data, sumRight[1] + node.data)

				return (maxSum, maxBranch)

		else:
			return (0, 0)

	def height(self, node, n):
		if node is not None:
			n += 1;
			if (node.left is None and node.right is None):
				return n
			else:
				return max(self.height(node.left, n), self.height(node.right, n));
		else:
			return 0

	def inOrder(self, node):
		if (node is not None):
			self.inOrder(node.left)
			print node.data
			self.inOrder(node.right)

	def repetitions(self, node, e):
		if (node is None):
			return 0
		else:
			if (node.data == e):
				return 1 + self.repetitions(node.left, e) + self.repetitions(node.right, e)
			else:
				return self.repetitions(node.left, e) + self.repetitions(node.right, e)

t = BinaryTree()
t.add(50)
t.add(40)
t.add(30)
t.add(20)
t.add(60)
t.add(70)
t.add(80)
# t.add(15)
# t.add(14)
# t.add(18)
# t.add(30)
# t.add(25)
# t.add(22)
# t.add(35)
# t.add(10)
# print 'repetitions of 5: ' + str(t.repetitions(t.root, 5))
print 'tree'
t.show(t.root)
# print 'inorder: '
# t.inOrder(t.root)
# t.mostRepeated(t.root, t.root.data, 0)
# print 'most repeated: ' + str(t.mostRepeatedAll)
# print 'lowest 14, 35: ' + str(t.lowestCommonAncestor(t.root, 2, 6))
print 'biggest sum: ' + str(t.biggestSum(t.root))



