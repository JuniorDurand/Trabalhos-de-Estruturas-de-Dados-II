from grafo import Grafo
from algoritmosDeOrdenacao import *
from utils import *

import argparse 
import time



'''
Implemente o algoritmo de ordenação no arquivo algoritmosDeOrdenacao.py
Instruções básicas de como fazer a implementação estão no arquivo algoritmosDeOrdenacao.py
'''

if __name__ == "__main__":


	parser = argparse.ArgumentParser()

	#definindo algoritmo usado
	parser.add_argument("algoritmo", type=str, help="Algoritmo de ordenacao")

	#definindo arquivo de entrada
	parser.add_argument("arquivo_entrada", type=str, help="Nome do arquivo de Entrada")

	#definindo arquivo de saida
	parser.add_argument("arquivo_saida", type=str, help="Nome do arquivo de Saída")

	#definido tamanho L da partição por inserção
	#argumento opcional deve ser utilizado apenas se o algoritmo selecionado
	#suportar inserção parcial ou final
	#deve ser digitado da seguinte forma:
	#Em algoritmos que suportam inserção parcial:
	# "main.py [algoritmo] [arquivo de entrada] [arquivo de saida] [-l  tamanho da partição por inserção]"

	#Em algoritmos que  NÃO suportam inserção parcial:
	# "main.py [algoritmo] [arquivo de entrada] [arquivo de saida]"
	parser.add_argument('-l', '--length', type=int, help="tamanho da partição por inserção")

	args = parser.parse_args()

	algoritmo = args.algoritmo
	length = args.length

	if length:

		if algoritmo.lower() == "mergesortpartialinsert":
			algoritmoDeOrdenacao = MergeSortPartialInsert(length)

		elif algoritmo.lower() == "mergesortfinalinsert":
			algoritmoDeOrdenacao = MergeSortFinalInsert(length)

		elif algoritmo.lower() == "quicksortpartialinsert":
			algoritmoDeOrdenacao = QuickSortPartialInsert(length)

		elif algoritmo.lower() == "quicksortfinalinsert":
			algoritmoDeOrdenacao = QuicksortFinalInsert(length)

		else:
			print("O algoritmo selecionado não suporta inserção parcial ou final")
			print("Algoritmos que suportão:")
			print("\tMergeSortPartialInsert")
			print("\tMergeSortFinalInsert")
			print("\tQuickSortPartialInsert")
			print("\tQuickSortFinalInsert")
			exit()

	else:

		if algoritmo.lower() == "insertionsort":
			algoritmoDeOrdenacao = InsertionSort()

		elif algoritmo.lower() == "selectionsort":
			algoritmoDeOrdenacao = SelectionSort()

		elif algoritmo.lower() == "shellsort":
			algoritmoDeOrdenacao = ShellSort()

		elif algoritmo.lower() == "mergesort":
			algoritmoDeOrdenacao = MergeSort()

		elif algoritmo.lower() == "quicksort":
			algoritmoDeOrdenacao = Quicksort()

		else:
			print("O algoritmo selecionado precisa do tamanho de partição para inserção")
			print("Digite da seguinte forma:")
			print("\tmain.py [algoritmo] [arquivo de entrada] [arquivo de saida] [-l  tamanho da partição por inserção]")
			print("\n\nExemplo:")
			print("\tmain.py QuicksortFinalInsert 7vertices.json out.txt -l 4")
			exit()




	arquivoJson = args.arquivo_entrada
	arquivoDeSaida = args.arquivo_saida

	grafo = Grafo()
	grafo.estabelecerAlgoritmoDeOrdencao(algoritmoDeOrdenacao)
	grafo.carregarGrafo(arquivoJson)

	arvoreGeradoraMinima =  grafo.executarKruskal() 
	SalvarArvoreGeradoraMinimaEmArquivo(arquivoDeSaida, arvoreGeradoraMinima)

