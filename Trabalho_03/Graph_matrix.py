class Graph(object):
	def __init__(self, size, oriented = "not_oriented"):
		self.oriented = oriented
		#self.adjMatrix = []
		self.adjMatrix = [[0 for x in range(size)] for y in range(size)] 
		for i in range(size):
			#self.adjMatrix[i] = []
			for j in range(size):
				self.adjMatrix[i][j] = None
		self.size = size

		#define predecessor
		self.pi = []
		for i in range(size):
			self.pi.append(None)

		
		self.alfa = []
		for i in range(size):
			self.alfa.append(None)

		self.dist = []
		for i in range(size):
			self.dist.append(None)
		

		self.cor = []
		for i in range(size):
			self.dist.append("branco")



	def addEDGE(self, u, v, weight = None):
		if self.oriented == "not_oriented":
			if weight == None:
				self.adjMatrix[u][v] = 1
				self.adjMatrix[v][u] = 1
			else:
				self.adjMatrix[u][v] = weight
				self.adjMatrix[v][u] = weight
		else:
			if weight == None:
				self.adjMatrix[u][v] = 1
			else:
				self.adjMatrix[u][v] = weight

	
	def removeEDGE(self, u, v):
		if self.oriented == "not_oriented":
			self.adjMatrix[u][v] = None
			self.adjMatrix[v][u] = None

		else:
			self.adjMatrix[u][v] = None

	
	def containsEDGE(self, u, v):
		return True if self.adjMatrix[u][v] != None else False


	def __len__(self):
		return self.size


	def __str__(self):
		string = "[\n"
		for row in  range(len(self.adjMatrix)) :
			string += "%d :\n" % (row)
			for val in range(len(self.adjMatrix[row])):
				if not self.adjMatrix[row][val] is None: 
					string += "\t %d, %.5f\n" % (val, self.adjMatrix[row][val]) 

		string += "]"
		return string
		



