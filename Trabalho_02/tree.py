
class TNode(object):

	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None






class BTree(object):
	"""docstring for BTree"""
	def __init__(self, CMPFunc = None, CMPKey = None):
		self.root = None
		if CMPFunc == None:
			self.cmp = self.defautCMP
		else:
			self.cmp = CMPFunc

		if CMPKey == None:
			self.cmpKey = self.defautCMP
		else:
			self.cmpKey = CMPKey

	def defautCMP(self, a, b):
		if (a > b):
			return -1
		elif(a < b):
			return 1
		else:
			return 0



	""" METODO PRIVADO DA INSERÇÃO """
	def __insert(self, data, Node):

		if Node != None:
			stat = self.cmp(Node.data, data)
			if stat < 0:
				Node.left = self.__insert(data, Node.left)
			else:
				Node.right = self.__insert(data, Node.right)

			return Node

		else:
			return TNode(data)


	""" METODO PUBLICO DA INSERÇÃO """
	def insert(self, data):
		self.root = self.__insert(data, self.root)

	

	""" MAIOR NÓ DA SUBÁRVORE ESQUERDA """
	def __maior(self, Node):
		if Node != None:
			if Node.right == None:
				if Node.right == None and Node.left == None:
					return Node, None
				else:
					return Node, Node.left

			else:
				Node, Node.right = self.__maior(Node.right)
				return Node


	""" METODO PRIVADO DA REMOÇÃO """
	def __remove(self, key,  cmpKey, Node):
		
		if Node != None:
			stat = cmpKey(Node.data, key)
			if stat < 0:
				data, Node.left = self.__remove(key,  cmpKey, Node = Node.left)
				return data, Node
			elif stat > 0:
				data, Node.right = self.__remove(key,  cmpKey, Node = Node.right)
				return data, Node
			else:
				data = Node.data
				if (Node.left == None and Node.right == None):
					return data, None

				elif (Node.left == None and Node.right != None):
					return data, Node.right

				elif (Node.left != None and Node.right == None):
					return data, Node.left

				else:
					CurNode, Node.right = self.__maior(Node.right)
					CurNode.left, CurNode.right = Node.left, Node.right
					return data, CurNode

	
	""" METODO PUBLICO DA REMOÇÃO """
	def remove(self, key, cmpKey):
		data, self.root = self.__remove(key, cmpKey, self.root)
		return data




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
			stat = self.cmpKey(Node.data, data)
			if stat < 0:
				return self.__insert(data, Node.left)
			elif stat > 0:
				return = self.__insert(data, Node.right)
			else:
				return Node.data


	def get(self, key):
		return self.__get(key, self.root)




		