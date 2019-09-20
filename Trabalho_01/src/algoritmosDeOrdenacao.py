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
			while i >= 0 and col[i]['weight'] > key['weight']:
				col[i+1] = col[i]
				i-=1

			col[i+1] = key
			
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
			if col[j]['weight'] < pivot['weight']:
				i+=1
				col[j], col[i] = col[i], col[j]

		if pivot['weight'] < col[i+1]['weight']:
			col[i+1], col[end] = col[end], col[i+1]

		return i +1



