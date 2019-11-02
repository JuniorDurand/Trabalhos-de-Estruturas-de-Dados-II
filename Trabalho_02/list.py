class Node(object):
	"""docstring for Node"""
	def __init__(self, data):
		self.data = data
		self.next = None		



class List(object):
	"""docstring for list"""
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

	def append(self, data):
		newNode = Node(data)
		newNode.next = self.first
		self.first = newNode
		self.len +=1



		