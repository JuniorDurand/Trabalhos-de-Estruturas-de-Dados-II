class Node(object):
	"""docstring for Node"""
	def __init__(self, data):
		self.data = data
		self.next = None		

	def __str__(self):
		return str(self.data)


class List(object):
	def __init__(self):
		self.first = None
		self.len = 0
		self.next = self.first

	def __len__(self):
		return self.len

	def __getitem__(self, posicao):
		count = 0
		cur = self.first
		while count != posicao and cur != None:
			cur = cur.next
			count +=1
		if cur != None and count==posicao:
			return cur.data

	def __iter__(self):
		cur = self.first
		while cur:
			yield cur.data
			cur = cur.next

	def __str__(self):
		string = "["
		cur = self.first
		while not cur is None:
			string += (str(cur)+", ")
			cur = cur.next
		
		string += "]"
		return string


	def __defaultCMP(self,data, key):
		if data == key:
			return True
		else:
			return False

	def append(self, data):
		newNode = Node(data)
		newNode.next = self.first
		self.first = newNode
		self.len +=1

	def get(self, key, cmp=None):
		if cmp == None:
			cmp = self.__defaultCMP

		cur  = self.first
		while not cur is None:
			if cmp(cur.data, key):
				return cur.data
			else:
				cur = cur.next
		return None




		