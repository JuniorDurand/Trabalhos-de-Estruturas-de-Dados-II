class TNode(object):

	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None
		self.h = 1

	def __str__(self):
		return str(self.data)

class  AvlTree(object):

	def __init__(self, funCMP=None, funCMPKey = None):
		self.root = None

		if funCMP is None:
			self.cmp = self.defautCMP
		else:
			self.cmp = funCMP

		if funCMPKey is None:
			self.cmpKey = self.defautCMP
		else:
			self.cmpKey = funCMPKey

	def avStr(self, Node, string):
		if not (Node == None):
			string1 = self.avStr(Node.left, string)
			string2 = (str(Node) + ", ")
			string3 = self.avStr(Node.right, string)
			return string1+string2+string3

		else:
			return ""


	def __str__(self):
		string = "["
		string += self.avStr( self.root, string)
		string += "]"

		return string

	def defautCMP(self, a, b):
		if (a > b):
			return -1
		elif(a < b):
			return 1
		else:
			return 0

	def __insert(self, data, Node):

		if Node == None:
			return TNode(data)
		else:
			stat = self.cmp(Node.data, data)

			if stat < 0:
				Node.left = self.__insert(data, Node.left)
			else:
				Node.right = self.__insert(data, Node.right)

			Node.h = 1 + max(self.__getH(Node.left), self.__getH(Node.right))

			bal = self.__getBalance(Node)

			if bal > 1 and self.cmp(Node.left.data, data ) < 0:
				return self.__rightRotation(Node)

			elif bal < -1 and self.cmp(Node.right.data, data) > 0:
				return self.__leftRotation(Node)

			elif bal > 1 and self.cmp(Node.left.data, data) > 0:
				Node.left = self.__leftRotation(Node.left)
				return self.__rightRotation(Node)

			elif bal < -1 and self.cmp(Node.right.data, data) < 0:
				Node.right = self.__rightRotation(Node.right)
				return self.__leftRotation(Node)

			else:
				return Node

	def insert(self, data):
		self.root = self.__insert(data, self.root)

	def __getH(self, Node):
		if Node is None:
			return 0
		else:
			return Node.h
			#return max(self.__getH(Node.right), self.__getH(Node.left)) + 1
		
	def __getBalance(self, Node):
		if Node is None:
			return 0
		else:
			return self.__getH(Node.left) - self.__getH(Node.right)

	def __leftRotation(self, Node):
		NodeAux = Node.right
		Node.right = NodeAux.left
		NodeAux.left = Node

		Node.h = 1 + max(self.__getH(Node.left), self.__getH(Node.right))
		NodeAux.h = 1 + max(self.__getH(NodeAux.left), self.__getH(NodeAux.right))


		return NodeAux

	def __rightRotation(self, Node):
		NodeAux = Node.left
		Node.left = NodeAux.right
		NodeAux.right = Node

		Node.h = 1 + max(self.__getH(Node.left), self.__getH(Node.right))
		NodeAux.h = 1 + max(self.__getH(NodeAux.left), self.__getH(NodeAux.right))

		return NodeAux

	

	def __visitSimet(self, funVisit, Node):

		if Node != None:
			self.__visitSimet(funVisit, Node.left)
			funVisit(Node.data)
			self.__visitSimet(funVisit, Node.right)

	def visitSimet(self, funVisit):
		if self.root != None:
			self.__visitSimet(funVisit, self.root)


	def __get(self, key, Node):

		if not Node is None:
			stat = self.cmpKey(Node.data, key)
			if stat == 0:
				return Node.data

			elif stat < 0:
				return self.__get(key, Node.left)

			else:
				return self.__get(key, Node.right)

		#return None
		return None



	def get(self, key):
		return self.__get(key, self.root)


