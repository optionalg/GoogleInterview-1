class BinaryTreeNode:

    def __init__(self, value):
        self.value = value
        self.left  = None
        self.right = None

    def insert_left(self, value):
        self.left = BinaryTreeNode(value)
        return self.left

    def insert_right(self, value):
        self.right = BinaryTreeNode(value)
        return self.right


class BinaryTree():
	
	def __init__(self):
		self.root = None
	def insert(self, val):
		if self.root == None:
			self.root = BinaryTreeNode(val)
		else:
			current = self.root
			while True:
				if current.value < val:
					if current.right != None:
						current = current.right
					else:
						current.right = BinaryTreeNode(val)
						break
				if current.value >= val:
					if current.left != None:
						current = current.left
					else:
						current.left = BinaryTreeNode(val)
						break

	def inOrder(self, current):
		if current.left != None:
			self.inOrder(current.left)
		print current.value
		if current.right != None:
			self.inOrder(current.right)

	def toString(self):
		self.inOrder(self.root)


import random
if __name__ == "__main__":
	
	tree = BinaryTree()
	for i in range(1,10):
		tree.insert( random.randint(1,20))
	tree.toString()		
