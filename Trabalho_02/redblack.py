class TNode(object):

	def __init__(self, data=None, left=None, right=None, parent=None, color=True):
		self.data = data
		self.left = left
		self.right = right
		self.parent = parent
		self.color = color #true is red; false is black

	def __str__(self):
		return str(self.data) +" "+ str(self.color) 

	def getColorDad(self):
		if not self.parent is None:
			return self.parent.color
		else:
			return False

	def getDad(self):
		return self.parent





class RedBlack(object):

	def __init__(self, funCMP=None, funCMPKey = None):
		self.__root = None

		if funCMP is None:
			self.cmp = self.defautCMP
		else:
			self.cmp = funCMP

		if funCMPKey is None:
			self.cmpKey = self.defautCMP
		else:
			self.cmpKey = funCMPKey

	def defautCMP(self, a, b):
		if (a > b):
			return -1
		elif(a < b):
			return 1
		else:
			return 0

	def getColor(self, Node):
		if not Node is None:
			return Node.color
		else:
			return False

	def __simmetric(self, node):
		if node is None:
			return
		self.__simmetric(node.right)
		print(node)
		self.__simmetric(node.left)
		
	def simmetric(self):
		self.__simmetric(self.__root)

	def __invertedIndex(self, node):
		if node is None:
			return
		self.__invertedIndex(node.left)
		print(node.data)
		self.__invertedIndex(node.right)

	def invertedIndex(self):
		if self.__root is None:
			print("Arvore Vazia")
			return None
		self.__invertedIndex(self.__root)
		
	def BSTInsert(self, data):
		if self.__root is None:
			self.__root = TNode(data, color=False)
			return self.__root
		else:
			aux = self.__root
			while aux is not None:
				aux2 = aux
				if self.cmp(aux.data , data) != -1:
					aux = aux.left
				else:
					aux = aux.right
					
			if self.cmp(aux2.data , data) != -1:
				aux2.left = TNode(data, parent=aux2)
				return aux2.left
			else:
				aux2.right = TNode(data, parent=aux2)
				return aux2.right
	
	def fixInsertion(self, node):
		parent_nd = None
		grand_parent_nd = None

		while (node != self.__root) and (node.color is not False) and (node.parent.color is True):
			parent_nd = node.parent
			grand_parent_nd = parent_nd.parent

			if node.parent == grand_parent_nd.left:
				uncle_nd = grand_parent_nd.right

				if uncle_nd is not None and uncle_nd.color is True:
					grand_parent_nd.color = True
					parent_nd.color = False
					uncle_nd.color = False
					node = grand_parent_nd
				else:
					if node == parent_nd.right:
						self.rotateLeft(parent_nd)
						node = parent_nd
						parent_nd = node.parent

					self.rotateRight(grand_parent_nd)
					aux = parent_nd.color
					parent_nd.color = grand_parent_nd.color
					grand_parent_nd.color = aux
					node = parent_nd
			else:
				uncle_nd = grand_parent_nd.left

				if uncle_nd is not None and uncle_nd.color is True:
					grand_parent_nd.color = True
					parent_nd.color = False
					uncle_nd.color = False
					node = grand_parent_nd
				else:
					if node == parent_nd.left:
						self.rotateRight(parent_nd)
						node = parent_nd
						parent_nd = node.parent

					self.rotateLeft(grand_parent_nd)
					aux = parent_nd.color
					parent_nd.color = grand_parent_nd.color
					grand_parent_nd.color = aux
					node = parent_nd

		self.__root.color = False
		
	def rotateLeft(self, node):
		nd_right = node.right
		node.right = nd_right.left

		if node.right is not None:
			node.right.parent = node

		nd_right.parent = node.parent

		if node.parent is None:
			self.__root = nd_right
		elif node == node.parent.left:
			node.parent.left = nd_right
		else:
			node.parent.right = nd_right

		nd_right.left = node
		node.parent = nd_right

	def rotateRight(self, node):
		nd_left = node.left
		node.left = nd_left.right

		if node.left is not None:
			node.left.parent = node

		nd_left.parent = node.parent

		if node.parent is None:
			self.__root = nd_left
		elif node == node.parent.left:
			node.parent.left = nd_left
		else:
			node.parent.right = nd_left

		nd_left.right = node
		node.parent = nd_left

	def insert(self, data):
		newnode = self.BSTInsert(data)

		self.fixInsertion(newnode)

	def __height(self, node):
		if node is None:
			return -1
		hl = 0
		hr = 0
		hl = self.__height(node.left)
		hr = self.__height(node.right)
		if hl > hr:
			return 1 + hl
		else:
			return 1 + hr
		
	def height(self):
		return self.__height(self.__root)
		
	def search(self, key):
		aux = self.__root
		while aux is not None:
			if self.cmpKey(aux.data, key) == 0:
				return aux.data
			if self.cmpKey(aux.data, key) == 1:
				aux = aux.left
			else:
				aux = aux.right

		return None
