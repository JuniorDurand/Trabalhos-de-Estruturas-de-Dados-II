class HashItem:
	def  __init__(self):
		self.key = None
		self.data = None
		self.stat = "None"

	def __str__(self):
		if (self.stat == "insert"):
			return("(" + str(self.key) + "," + str(self.data)+")")
		else:
			return ""

	def __repr__(self):
		if (self.stat == "insert"):
			return("(" + str(self.key) + "," + str(self.data)+")")
		else:
			return ""

	def insert(self, key, data):
		self.key = key
		self.data = data
		self.stat = "insert"

	def remove(self):
		self.key = None
		self.data = None
		self.stat = "remove"




class HashTable(object):
	def __init__(self, len=37):
		self.len = len
		self.numItens = 0
		self.lista = []
		for i in range(self.len):
			self.lista.append(HashItem())

	def __str__(self):
		strObj = "["
		for x in self.lista:
			strObj += x.__str__()
		return strObj+"]"

	def __repr__(self):
		strObj = "["
		for x in self.lista:
			strObj += x.__repr__()
		return strObj+"]"


	def insert(self, key, data):
		if self.numItens < int(self.len*0.7):
			posi = hash(key)%self.len
			initPosi = posi
			while self.lista[posi].stat == 'insert':
				if self.lista[posi].key == key:
					break
				posi = posi+1%self.len

			self.lista[posi].insert(key, data)
			self.numItens +=1
		else:
			#print("NewHash")
			NewHash = HashTable(len=self.len*37)
			for x in range(self.len):
				if self.lista[x].stat == 'insert':
					NewHash.insert(self.lista[x].key, self.lista[x].data)
			NewHash.insert(key, data)
			self.len = NewHash.len
			self.numItens = NewHash.numItens
			self.lista = NewHash.lista

	def get(self, key):
		posi = hash(key)%self.len
		initPosi = posi
		while self.lista[posi].key != key:
			if self.lista[posi].stat == "None":
				return None
			else:
				posi = posi+1%self.len
				if initPosi == posi:
					return None

		return self.lista[posi].data

	def remove(self, key):
		posi = hash(key)%self.len
		initPosi = posi
		while self.lista[posi].key != key:
			if self.lista[posi].stat == "None":
				return None
			else:
				posi = posi+1%self.len
				if initPosi == posi:
					return None

		data = self.lista[posi].data
		self.lista[posi].remove()
		self.numItens -=1
		return data


		