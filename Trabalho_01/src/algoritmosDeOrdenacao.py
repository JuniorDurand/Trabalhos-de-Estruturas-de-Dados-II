'''
Introdução:
- Implementar algoritmo de ordenação que receba uma colecão
- A coleção é uma lista de arestas
- Para comparar o peso as arestas entre dois item da coleção basta usar a chave 'weight' (peso)

Exemplos:
- Modo convencional
colecao[i] operador de comparacao colecao[j]
colecao[i] < colecao[j]

- Modo que você vai usar
int(colecao[i]['weight']) operador de comparacao int(colecao[j]['weight'])
int(colecao[i]['weight']) < int(colecao[j]['weight'])

É nescessário converter o valor pra Interger no momento da comparação a fim de evitar erros
'''


# Sua classe algoritmo de ordenação precisar ter um método ordenar
"""
class InsertionSort(object):
    def ordenar(self, colecao):
        '''
        O método ordenar recebe uma colecão
        realiza ordenacão na colecão
        retorna colecão após ordenação
        '''
        return colecao
"""
class InsertionSort(object):

	def ordenar( self, col, start=0,  end=None):
		if end == None:
			end = len(col)
			
		for j in range(start,end):
			key = col[j]

			i = j -1
			while i >= 0 and int(col[i]['weight']) > int(key['weight']):
				col[i+1] = col[i]
				i-=1

			col[i+1] = key
			
		return col



class SelectionSort(object):

	def ordenar( self, col, start=0,  end=None):
		if end == None:
			end = len(col)
			
		for i in range(start,end):
			min = i
			for j in range(i+1, end):
				if int(col[j]['weight']) < int(col[min]['weight']) :
					min = j

			temp = col[min]
			col[min] = col[i]
			col[i] = temp

		return col



class ShellSort(object):

	def ordenar( self, col, start=0,  end=None):
		if end == None:
			end = len(col)
			
		h = 1
		while h < end - start:
			h = (3*h)+1

		while h > 0:
			h = (h-1)//3

			for i in range(h, end - start):
				temp = col[i]
				j=i

				while int(col[j-h]['weight']) > int(temp['weight']):
					col[j] = col[j-h]
					j = j - h
					if (j < h):
						break

				col[j] = temp

		return col

class MergeSort(object):



	def ordenar(self,  col, start = 0, end = None): 
		if len(col) >1:
			mid = len(col)//2 
			colL = col[:mid]  
			colR = col[mid:]

			self.ordenar(colL) 
			self.ordenar(colR) 

			i = 0
			j = 0
			k = 0

			while i < len(colL) and j < len(colR): 
				if int(colL[i]['weight']) < int(colR[j]['weight']): 
					col[k] = colL[i] 
					i+=1
				else: 
					col[k] = colR[j] 
					j+=1
				k+=1

			while i < len(colL): 
				col[k] = colL[i] 
				i+=1
				k+=1

			while j < len(colR): 
				col[k] = colR[j] 
				j+=1
				k+=1


class MergeSortPartialInsert(object):

	def __init__(self, L):
		self.insert = InsertionSort()
		self.L = L

	
	def setL(self, L):
		self.L = L

	
	def ordenar(self,  col, start = 0, end = None): 
		if len(col) >1:
			mid = len(col)//2 
			colL = col[:mid] 
			colR = col[mid:] 

			if len(colL) < self.L:
				self.insert.ordenar(colL)
			else:
				self.ordenar(colL)

			if len(colR) < self.L:
				self.insert.ordenar(colR)
			else:
				self.ordenar(colR) 

			i = 0
			j = 0
			k = 0

			while i < len(colL) and j < len(colR): 
				if int(colL[i]['weight']) < int(colR[j]['weight']): 
					col[k] = colL[i] 
					i+=1
				else: 
					col[k] = colR[j] 
					j+=1
				k+=1

			
			while i < len(colL): 
				col[k] = colL[i] 
				i+=1
				k+=1

			while j < len(colR): 
				col[k] = colR[j] 
				j+=1
				k+=1

		return col



class MergeSortFinalInsert(object):

	def __init__(self, L):
		self.insert = InsertionSort()
		self.L = L

	
	def setL(self, L):
		self.L = L

	
	def ordenar(self,  col, start = 0, end = None, chamada=0): 
		if len(col) >1:
			mid = len(col)//2 
			colL = col[:mid]
			colR = col[mid:]

			if not (len(colL) < self.L and len(colR) < self.L):
				self.ordenar(colL, chamada= chamada+1)
				self.ordenar(colR, chamada= chamada+1) 
			
				


			i = 0
			j = 0
			k = 0

			while i < len(colL) and j < len(colR): 
				if int(colL[i]['weight']) < int(colR[j]['weight']): 
					col[k] = colL[i] 
					i+=1
				else: 
					col[k] = colR[j] 
					j+=1
				k+=1

			# Checking if any element was left 
			while i < len(colL): 
				col[k] = colL[i] 
				i+=1
				k+=1

			while j < len(colR): 
				col[k] = colR[j] 
				j+=1
				k+=1

			if chamada == 0:
				print(col)
				self.insert.sort(col)
				print(col)

		return col



class Quicksort(object):

	def ordenar( self, col, start=0,  end=None):
		if end == None:
			end = len(col) -1
		
		if start < end:
			part = self.partition(col, start, end)
			self.ordenar(col, start, part-1)
			self.ordenar(col, part+1, end)

		return col

	def partition(self, col, start, end):
		pivot = col[end]
		i = start-1

		for j in range(start, end):
			if int(col[j]['weight']) < int(pivot['weight']):
				i+=1
				col[j], col[i] = col[i], col[j]

		if int(pivot['weight']) < int(col[i+1]['weight']):
			col[i+1], col[end] = col[end], col[i+1]

		return i +1


class QuickSortPartialInsert(object):

	def __init__(self, L):
		self.insert = InsertionSort()
		self.L = L

	def setL(self, L):
		self.L = L

	def ordenar( self, col, start=0,  end=None):
		if end == None:
			end = len(col) -1
		
		if start < end:
			part = self.partition(col, start, end)

			if part - start < self.L :
				self.insert.ordenar(col, start, part)
			else:
				self.ordenar(col, start, part-1)

			if end - part < self.L:		
				self.insert.ordenar(col, part +1, end)
			else:
				self.ordenar(col, part+1, end)

		return col

	def partition(self, col, start, end):
		pivot = col[end]
		i = start-1

		for j in range(start, end):
			if int(col[j]['weight']) < int(pivot['weight']):
				i+=1
				col[j], col[i] = col[i], col[j]

		if int(pivot['weight']) < int(col[i+1]['weight']):
			col[i+1], col[end] = col[end], col[i+1]

		return i +1




class QuicksortFinalInsert(object):

	def __init__(self, L):
		self.insert = InsertionSort()
		self.L = L

	def setL(self, L):
		self.L = L

	def ordenar( self, col, start=0,  end=None, chamada=0):
		if end == None:
			end = len(col) -1
		
		if start < end:
			part = self.partition(col, start, end)

			if part-1 - start > self.L:
				self.ordenar(col, start, part-1, chamada=chamada+1)

			if end - part+1 > self.L:
				self.ordenar(col, part+1, end, chamada=chamada+1)

		if chamada == 0:
			self.insert.ordenar(col)

		return col

	def partition(self, col, start, end):
		pivot = col[end]
		i = start-1

		for j in range(start, end):
			if int(col[j]['weight']) < int(pivot['weight']):
				i+=1
				col[j], col[i] = col[i], col[j]

		if int(pivot['weight']) < int(col[i+1]['weight']):
			col[i+1], col[end] = col[end], col[i+1]

		return i +1




