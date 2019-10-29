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

	def __init__(self):
		#quantificando atribuições e comparações
		self.cmp = 0
		self.atb = 0

	def summary(self):
		print("comparações: ", self.cmp)
		print("atribuições: ", self.atb)

	def ordenar( self, col, start=0,  end=None):
		if end == None:
			end = len(col)
			self.cmp += 1
			self.atb += 1
			
		for j in range(start,end):
			key = col[j]
			self.cmp += 1
			self.atb += 2

			i = j -1
			self.atb +=1
			while i >= 0 and int(col[i]['weight']) > int(key['weight']):
				col[i+1] = col[i]
				i-=1
				self.cmp += 2
				self.atb += 2

			col[i+1] = key
			self.atb += 1
			
		return col



class SelectionSort(object):

	def __init__(self):
		#quantificando atribuições e comparações
		self.cmp = 0
		self.atb = 0

	def summary(self):
		print("comparações: ", self.cmp)
		print("atribuições: ", self.atb)


	def ordenar( self, col, start=0,  end=None):
		if end == None:
			end = len(col)
			self.cmp += 1
			self.atb += 1
			
		for i in range(start,end):
			min = i
			self.cmp += 1
			self.atb += 2
			for j in range(i+1, end):
				self.cmp += 1
				self.atb += 1

				self.cmp += 1
				if int(col[j]['weight']) < int(col[min]['weight']) :
					min = j
					self.atb += 1

			temp = col[min]
			col[min] = col[i]
			col[i] = temp
			self.atb += 3

		return col



class ShellSort(object):

	def __init__(self):
		#quantificando atribuições e comparações
		self.cmp = 0
		self.atb = 0

	def summary(self):
		print("comparações: ", self.cmp)
		print("atribuições: ", self.atb)

	
	def ordenar( self, col, start=0,  end=None):
		self.cmp += 1
		if end == None:
			end = len(col)
			self.atb += 1
			
		h = 1
		self.atb += 1
		
		self.cmp += 1
		while h < end - start:
			h = (3*h)+1
			self.atb += 1

		self.cmp += 1
		while h > 0:
			h = (h-1)//3
			self.atb += 1

			for i in range(h, end - start):
				temp = col[i]
				j=i
				self.cmp += 1
				self.atb += 3

				while int(col[j-h]['weight']) > int(temp['weight']):
					col[j] = col[j-h]
					j = j - h
					self.atb += 3
					self.cmp += 2
					if (j < h):
						break

				col[j] = temp
				self.atb += 1

		return col

class MergeSort(object):

	def __init__(self):
		#quantificando atribuições e comparações
		self.cmp = 0
		self.atb = 0

	def summary(self):
		print("comparações: ", self.cmp)
		print("atribuições: ", self.atb)



	def ordenar(self,  col, start = 0, end = None, chamada=0): 
		
		self.cmp+=1
		if len(col) >1:
			mid = len(col)//2 
			self.atb+=1
			colL = col[:mid]  
			colR = col[mid:]

			colL = self.ordenar(colL, chamada=chamada+1) 
			colR = self.ordenar(colR, chamada=chamada+1) 

			i = 0
			j = 0
			k = 0
			self.atb+=3



			while i < len(colL) and j < len(colR): 
				self.cmp+=2
				if int(colL[i]['weight']) < int(colR[j]['weight']): 
					col[k] = colL[i] 
					i+=1
					self.atb+=2
				else: 
					col[k] = colR[j] 
					j+=1
					self.atb+=2
				k+=1
				self.atb+=1

			while i < len(colL):
				self.cmp+=1
				col[k] = colL[i] 
				i+=1
				k+=1
				self.atb+=3

			while j < len(colR): 
				self.cmp+=1
				col[k] = colR[j] 
				j+=1
				k+=1
				self.atb+=3


		return col


class MergeSortPartialInsert(object):

	def __init__(self, L):
		self.insert = InsertionSort()
		self.L = L
		#quantificando atribuições e comparações
		self.cmp = 0
		self.atb = 0


	def summary(self):
		print("sumario insert:")
		self.insert.summary()
		print("sumario merger:")
		print("comparações: ", self.cmp)
		print("atribuições: ", self.atb)


	
	def setL(self, L):
		self.L = L

	
	def ordenar(self,  col, start = 0, end = None):
		self.cmp+=1
		if len(col) >1:
			mid = len(col)//2 
			self.atb+=1
			colL = col[:mid] 
			colR = col[mid:] 

			self.cmp+=1
			if len(colL) < self.L:
				colL = self.insert.ordenar(colL)
			else:
				colL = self.ordenar(colL)

			self.cmp+=1
			if len(colR) < self.L:
				colR = self.insert.ordenar(colR)
			else:
				colR = self.ordenar(colR) 

			i = 0
			j = 0
			k = 0
			self.atb+=3

			while i < len(colL) and j < len(colR): 
				self.cmp+=2
				if int(colL[i]['weight']) < int(colR[j]['weight']): 
					col[k] = colL[i] 
					i+=1
					self.atb+=2
				else: 
					col[k] = colR[j] 
					j+=1
					self.atb+=2
				k+=1
				self.atb+=1

			
			while i < len(colL): 
				self.cmp+=1
				col[k] = colL[i] 
				i+=1
				k+=1
				self.atb+=3

			while j < len(colR): 
				self.cmp+=1
				col[k] = colR[j] 
				j+=1
				k+=1
				self.atb+=3

		return col



class MergeSortFinalInsert(object):

	def __init__(self, L):
		self.insert = InsertionSort()
		self.L = L
		#quantificando atribuições e comparações
		self.cmp = 0
		self.atb = 0


	def summary(self):
		print("sumario insert:")
		self.insert.summary()
		print("sumario merger:")
		print("comparações: ", self.cmp+self.insert.cmp)
		print("atribuições: ", self.atb+self.insert.atb)


	
	def setL(self, L):
		self.L = L

	
	def ordenar(self,  col, start = 0, end = None, chamada=0):
		self.cmp+=1
		if len(col) >1:
			mid = len(col)//2 
			self.atb+=1
			colL = col[:mid]
			colR = col[mid:]

			self.cmp+=1
			if not (len(colL) < self.L and len(colR) < self.L):
				self.ordenar(colL, chamada= chamada+1)
				self.ordenar(colR, chamada= chamada+1) 
			
				


			i = 0
			j = 0
			k = 0
			self.atb+=3

			while i < len(colL) and j < len(colR): 
				self.cmp+=2
				if int(colL[i]['weight']) < int(colR[j]['weight']): 
					col[k] = colL[i] 
					i+=1
				else: 
					col[k] = colR[j] 
					j+=1
				k+=1

			# Checking if any element was left 
			while i < len(colL):
				self.cmp+=1 
				col[k] = colL[i] 
				i+=1
				k+=1
				self.atb+=3 

			while j < len(colR): 
				self.cmp+=1 
				col[k] = colR[j] 
				j+=1
				k+=1
				self.atb+=1 

			if chamada == 0:
				self.insert.ordenar(col)

		return col



class Quicksort(object):

	def __init__(self):
		#quantificando atribuições e comparações
		self.cmp = 0
		self.atb = 0

	def summary(self):
		print("comparações: ", self.cmp)
		print("atribuições: ", self.atb)


	def ordenar( self, col, start=0,  end=None):
		self.cmp+=1
		if end == None:
			end = len(col) -1
			self.atb+=1
		
		self.cmp+=1
		if start < end:
			part = self.partition(col, start, end)
			self.atb+=1
			self.ordenar(col, start, part-1)
			self.ordenar(col, part+1, end)

		return col

	def partition(self, col, start, end):
		pivot = col[end]
		i = start-1
		self.atb+=2

		for j in range(start, end):
			self.atb+=1
			self.cmp+=2
			if int(col[j]['weight']) < int(pivot['weight']):
				i+=1
				col[j], col[i] = col[i], col[j]
				self.atb+=3

		self.cmp+=1
		if int(pivot['weight']) < int(col[i+1]['weight']):
			col[i+1], col[end] = col[end], col[i+1]
			self.atb+=2

		return i +1


class QuickSortPartialInsert(object):

	def __init__(self, L):
		self.insert = InsertionSort()
		self.L = L
		#quantificando atribuições e comparações
		self.cmp = 0
		self.atb = 0


	def summary(self):
		print("sumario insert:")
		self.insert.summary()
		print("sumario Quick:")
		print("comparações: ", self.cmp)
		print("atribuições: ", self.atb)

	def setL(self, L):
		self.L = L

	def ordenar( self, col, start=0,  end=None):
		self.cmp+=1
		if end == None:
			end = len(col) -1
			self.atb+=1
		
		self.cmp+=1
		if start < end:
			self.atb+=1
			part = self.partition(col, start, end)

			self.cmp+=1
			if part - start < self.L :
				self.insert.ordenar(col, start, part)
			else:
				self.ordenar(col, start, part-1)

			self.cmp+=1
			if end - part < self.L:		
				self.insert.ordenar(col, part +1, end)
			else:
				self.ordenar(col, part+1, end)

		return col

	def partition(self, col, start, end):
		pivot = col[end]
		i = start-1
		self.atb+=2

		for j in range(start, end):
			self.atb+=1
			self.cmp+=2
			if int(col[j]['weight']) < int(pivot['weight']):
				i+=1
				col[j], col[i] = col[i], col[j]
				self.atb+=3

		self.cmp+=1
		if int(pivot['weight']) < int(col[i+1]['weight']):
			col[i+1], col[end] = col[end], col[i+1]
			self.atb+=2

		return i +1




class QuicksortFinalInsert(object):

	def __init__(self, L):
		self.insert = InsertionSort()
		self.L = L
		#quantificando atribuições e comparações
		self.cmp = 0
		self.atb = 0


	def summary(self):
		print("sumario insert:")
		self.insert.summary()
		print("sumario Quick:")
		print("comparações: ", self.cmp+self.insert.cmp)
		print("atribuições: ", self.atb+self.insert.atb)

	def setL(self, L):
		self.L = L

	def ordenar( self, col, start=0,  end=None, chamada=0):
		self.cmp+=1
		if end == None:
			end = len(col) -1
			self.atb+=1
		
		self.cmp+=1
		if start < end:
			part = self.partition(col, start, end)
			self.atb+=1

			self.cmp+=1
			if part-1 - start > self.L:
				self.ordenar(col, start, part-1, chamada=chamada+1)

			self.cmp+=1
			if end - part+1 > self.L:
				self.ordenar(col, part+1, end, chamada=chamada+1)

		self.cmp+=1
		if chamada == 0:
			self.insert.ordenar(col)

		return col

	def partition(self, col, start, end):
		pivot = col[end]
		i = start-1
		self.atb+=2

		for j in range(start, end):
			self.atb+=1
			self.cmp+=2
			if int(col[j]['weight']) < int(pivot['weight']):
				i+=1
				col[j], col[i] = col[i], col[j]
				self.atb+=3

		self.cmp+=1
		if int(pivot['weight']) < int(col[i+1]['weight']):
			col[i+1], col[end] = col[end], col[i+1]
			self.atb+=2

		return i +1




