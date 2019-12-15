import heapq
import sys

class EDGE(object):
	"""docstring for EDGE"""
	def __init__(self, weight, u, v):
		self.weight = weight
		self.u = u
		self.v = v

	def __str__(self):
		return "[%d , %d -> %d]" % (self.weight, self.u.num, self.v.num)


	def __repr__(self):
		return "[%d , %d -> %d]" % (self.weight, self.u.num, self.v.num)        


	def __eq__( a, b):
		if (a.u == b.v or a.v == b.u) or (a.u == b.u and a.v == b.v):
			return True
		else:
			return False

	def __ne__( a, b):
		if (a.u == b.v or a.v == b.u) or (a.u == b.u and a.v == b.v):
			return False
		else:
			return True

	def __lt__( a, b):
		return  a.weight < b.weight

	def __le__( a, b):
		return  a.weight <= b.weight
	
	def __ge__( a, b):
		return a.weight >= b.weight

	def __gt__( a, b):
		return a.weight > b.weight
		





class Vertex(object):
	def __init__(self, num):
		self.num = num
		self.listAdj = []
		self.listWeight = []
		self.pi = None
		self.alfa = None
		self.dist = None
		self.cor = "branco"


	#definindo operadores para algoritmo de Dijkstra
	def __lt__( a, b):
		return  a.dist < b.dist

	def __le__( a, b):
		return  a.dist <= b.dist
	
	def __ge__( a, b):
		return a.dist >= b.dist

	def __gt__( a, b):
		return a.dist > b.dist

	def __eq__( a, b):
		return a.num == b.num

	def __ne__( a, b):
		return a.num != b.num


	def resetVertex(self):
		self.pi = None
		self.alfa = None
		self.dist = None
		self.cor = "branco"


	def addEDGE(self, edge, weight=1):
		self.listAdj.append(edge)
		self.listWeight.append(weight)


	def removeEDGE(self, edge):
		index = self.listAdj.index(edge)
		if not index is None:
			self.listAdj.pop(index)
			self.listWeight.pop(index)


	def containsEDGE(self, edge):
		if edge in self.listAdj:
			return True
		else:
			return False


	def getEDGEs(self):
		EDGEs = []
		for x in self.listAdj:
			EDGEs.append(x)

		return EDGEs



	def getEDGEsObj(self):
		EDGEs = []
		for x in range(len(self.listAdj)):
			Edge = EDGE(self.listWeight[x], self, self.listAdj[x])
			EDGEs.append(Edge)

		return EDGEs

	def updateEDGE(self, edge, weight=1):
		index = self.listAdj.index(edge)
		if not index is None:
			self.listWeight[index] = weight
	

	def order(self, vertex):
		return vertex.num


	def ordenedVertex(self):
		self.listAdj.sort(key = self.order, reverse=True)


	def __str__(self):
		#self.ordenedVertex()
		string = ""
		string += "%d :\n" % (self.num)
		for x in range(len(self.listAdj)):
			string += "\t %d, %.5f\n" % (self.listAdj[x].num, self.listWeight[x]) 
		return string


	def __repr__(self):
		string = ""
		string += "\n%d: " % (self.num)
		for x in self.listAdj[::-1]:
			string += "%d " % (x.num) 
		return string
		

class Graph(object):
	
	def __init__(self, size, oriented = "not_oriented"):
		self.oriented = oriented
		self.vertex = []
		for i in range(size):
			self.vertex.append(Vertex(num=i))
		self.size = size


	def resetGraph(self):
		for x in self.vertex:
			x.resetVertex()


	def addEDGE(self, u, v, weight = None):
		if not self.containsEDGE(u, v):
			if self.oriented == "not_oriented":
				if weight == None:
					self.vertex[u].addEDGE(self.vertex[v])
					self.vertex[v].addEDGE(self.vertex[u])
				else:
					self.vertex[u].addEDGE(self.vertex[v], weight = weight)
					self.vertex[v].addEDGE(self.vertex[u], weight = weight)
			else:
				if weight == None:
					self.vertex[u].addEDGE(self.vertex[v])
				else:
					self.vertex[u].addEDGE(self.vertex[v], weight = weight)
		else:
			self.updateEDGE(u, v, weight)

	
	def removeEDGE(self, u, v):
		if self.oriented == "not_oriented":
			self.vertex[u].removeEDGE(self.vertex[v])
			self.vertex[v].removeEDGE(self.vertex[u])
		else:
			self.vertex[u].removeEDGE(self.vertex[v])


	def updateEDGE(self, u, v, weight = 1):
		if self.containsEDGE(u,v):
			if self.oriented == "not_oriented":
				self.vertex[u].updateEDGE(self.vertex[v], weight)
				self.vertex[v].updateEDGE(self.vertex[u], weight)
			else:
				self.vertex[u].updateEDGE(self.vertex[v], weight)



	
	def containsEDGE(self, u, v):
		return True if self.vertex[u].containsEDGE(self.vertex[v]) == True else False


	def __len__(self):
		return self.size


	def __str__(self):
		string = "[\n"
		for row in self.vertex:
			string += row.__str__()

		string += "]"
		return string

	def __repr__(self):
		string = ""
		for row in self.vertex:
			string += row.__repr__()

		string += ""
		return string


	def BFS(self, u = None):
		self.resetGraph()
		if u is None:
			u = self.vertex[0]
		else:
			u = self.vertex[u]

		queue = []
		#dist, Vertex.
		queue.append([0,u])
		while len(queue) > 0:
			#print(queue)
			count, u = queue.pop()
			EDGEs = u.getEDGEs()
			for EDGE in EDGEs:
				if EDGE.cor == "branco":
					queue.append([count+1,EDGE])
					EDGE.cor = "cinza"
					EDGE.dist = count+1
					EDGE.pi = u
			u.cor = "preto"



	def eccentricity(self, u = None):
		self.resetGraph()
		if u is None:
			u = self.vertex[0]
		else:
			u = self.vertex[u]

		max = [0, None]

		queue = []
		#dist, Vertex.
		queue.append([0,u])

		while len(queue) > 0:
			#print(queue)
			count, u = queue.pop()
			EDGEs = u.getEDGEs()
			for EDGE in EDGEs:
				if EDGE.cor == "branco":
					queue.append([count+1,EDGE])
					EDGE.cor = "cinza"
					EDGE.dist = count+1
					EDGE.pi = u

					# para excentricidade
					if max[0] <= count+1:
						max = [count+1, EDGE]
			u.cor = "preto"
		return max[0]

	def eccentricityVertex(self, u = None):
		self.resetGraph()
		if u is None:
			u = self.vertex[0]
		elif u is int:
			u = self.vertex[u]

		max = [0, None]

		queue = []
		#dist, Vertex.
		queue.append([0,u])

		while len(queue) > 0:
			#print(queue)
			count, u = queue.pop()
			EDGEs = u.getEDGEs()
			for EDGE in EDGEs:
				if EDGE.cor == "branco":
					queue.append([count+1,EDGE])
					EDGE.cor = "cinza"
					EDGE.dist = count+1
					EDGE.pi = u

					# para excentricidade
					if max[0] <= count+1:
						max = [count+1, EDGE]
			u.cor = "preto"
		return max[0]


	def Diameter(self):
		maxEcc = self.eccentricityVertex(u = self.vertex[0])
		for EDGE in self.vertex[1:]:
			x = self.eccentricityVertex(u = EDGE)
			if x > maxEcc:
				maxEcc = x
		return maxEcc


	def Radius(self):
		minEcc = self.eccentricityVertex(u = self.vertex[0])
		for EDGE in self.vertex[1:]:
			x = self.eccentricityVertex(u = EDGE)
			if x < minEcc:
				minEcc = x
		return minEcc


	def BFS_orig_dest(self, u, v):
		self.BFS(u)
		vertDest = self.vertex[v]
		return vertDest.dist
		"""string = ""
		while not vertDest is None:
			string += ("->" + str(vertDest.num)) 
			vertDest = vertDest.pi

		print(string)"""


	def SecurityEDGEPrim(self, EDGE):
		if EDGE.u.cor != "preto" or EDGE.v.cor != "preto":
			return True
		else:
			return False

	def SecurityEDGEsPrim(self, listEDGEs):
		lista = []
		for EDGE in listEDGEs:
			if self.SecurityEDGEPrim(EDGE):
				lista.append(EDGE)
		return lista





	def Prim(self, u):
		self.resetGraph()
		self.MTS = Graph(self.size)
		u = self.vertex[u]
		init = u
		components = []
		components.append(u)
		u.cor = "preto"
		EDGEs = u.getEDGEsObj()
		while len(EDGEs) > 0:
			EDGEs = self.SecurityEDGEsPrim(EDGEs)
			heapq.heapify(EDGEs)
			EDGE = heapq.heappop(EDGEs)
			self.MTS.addEDGE(EDGE.u.num, EDGE.v.num, weight= EDGE.weight)
			if EDGE.u.cor != "preto":
				components.append(EDGE.u)
				EDGE.u.cor = "preto"
			if EDGE.v.cor != "preto":
				EDGE.v.cor = "preto"
				components.append(EDGE.v)

			EDGEs = []
			for x in components:
				EDGEs.extend(x.getEDGEsObj())

			EDGEs = self.SecurityEDGEsPrim(EDGEs)

	def RemoveDuplicate(self, lista):
		final_list = []
		for num in lista:
			if num not in final_list:
				final_list.append(num)
		return final_list 

	def SecurityEDGEKruskal(self, u, v):
		if u.alfa != v.alfa:
			return True
		else:
			return False

	def MergeComponents(self, components, u, v):
		u = u.alfa
		v = v.alfa
		while len(components[v]) > 0:
			component = components[v].pop()
			component.alfa = u
			components[u].append(component)


	def Kruskal(self):
		self.resetGraph()
		self.MTS = Graph(self.size)
		components = []
		for x in range(self.size):
			components.insert(x, [])
			#components[x] = []
			components[x].append(self.vertex[x])
			self.vertex[x].alfa = x

		EDGEs = []
		for vertex in self.vertex:
			EDGEs.extend(vertex.getEDGEsObj())
		self.RemoveDuplicate(EDGEs)

		EDGEs.sort()

		while len(EDGEs) > 0:
			Edge = EDGEs.pop(0)
			if self.SecurityEDGEKruskal(Edge.u, Edge.v):
				self.MergeComponents(components, Edge.u, Edge.v)
				self.MTS.addEDGE(Edge.u.num, Edge.v.num, weight= Edge.weight)

	

	def SecurityVertexDijkstra(self, EDGE):
		if EDGE.cor != "preto":
			return True
		else:
			return False

	def SecurityVertexsDijkstra(self, listEDGEs):
		lista = []
		for EDGE in listEDGEs:
			if self.SecurityVertexDijkstra(EDGE):
				lista.append(EDGE)
		return lista


	def Relax(self, u):
		count = 0
		for EDGE in u.listAdj:
			if EDGE.dist > u.dist + u.listWeight[count]:
				EDGE.dist = u.dist + u.listWeight[count]
				EDGE.pi = u
			count += 1




	def Dijkstra(self, u):
		self.resetGraph()
		
		for x in self.vertex:
			x.dist = sys.maxsize

		u = self.vertex[u]
		u.dist = 0

		EDGEs = []
		EDGEs.append(u)
		
		while len(EDGEs) > 0:
			EDGEs.sort()
			u = EDGEs.pop(0)
			EDGEs.extend(u.getEDGEs())
			u.cor = "preto"
			self.Relax(u)
			EDGEs = self.SecurityVertexsDijkstra(EDGEs)
			EDGEs = self.RemoveDuplicate(EDGEs)


	def DistMenor(self, orig, dist):
		lista = []
		self.Dijkstra(orig)
		for vert in self.vertex:
			if vert.dist <= dist:
				lista.append(vert.num)
		return lista








