from Graph_list import Graph as Graph_ls
from Graph_matrix import Graph as Graph_mx
import heapq
import sys


from utils import *

import argparse 
import time




if __name__ == "__main__":

	parser = argparse.ArgumentParser()

	#definindo arquivo de entrada
	parser.add_argument("arquivo", type=str, help="Arquivo com o grafo")



	#utilizar da seguinte forma:
	# "main.py [arquivo com o grafo]"


	args = parser.parse_args()

	arquivo = args.arquivo

	print("O grafo é orientado? (1-SIM/0-NÃO)")
	orient = int(input())
	print("Como o grafo deve ser representado? (1 - LISTA de ADJ / 0 - MATRIZ de ADJ)")
	repre = int(input())
	
	if orient == 1:
		orient = "oriented"
	else:
		orient = "not_oriented"

	print("Carregando arquivo")
	if repre == 1:
		grafo = readGraphList(arquivo, orient)
	else:
		grafo = readGraphMatrix(arquivo, orient)


	if not grafo is None:
		print("arquivo carregado")
	else:
		print("arquivo não carregado")
		exit()

	opcao = -1
	while opcao != 0:
		print("=====MENU=====")
		print("0 - SAIR")
		print("1 - BUSCA EM LARGURA (NUMERO DE VERTICES DA ORIGEM AO DESTINO)")
		print("2 - IMPRIMIR GRAFO AO INVERSO DA ORDEM DE CARREGAMENTO")
		print("3 - CALCULA A EXCENTRICIDADE DE UM VÉRTICE V")
		print("4 - CALCULA O DIÂMETRO DO GRAFO")
		print("5 - CALCULA O RAIO DO GRAFO")
		print("6 - MST POR PRIM")
		print("7 - MST POR KRUSKAL")
		print("8 - VERTICES COM DISTANCIA MENOR QUE X")

		opcao = int(input())

		if opcao == 1:
			if repre == 1:
				orig = int(input("Vertice de origem:"))
				dest = int(input("Vertice de destino:"))
				dist = grafo.BFS_orig_dest( orig, dest)
				print("A quantidade de arestas do vertice ", orig, "até o vertice ", dest," é ", dist)


			else:
				print("Algoritmo não implementado para esta representação")

		elif opcao == 2:
			print(grafo)

		elif opcao == 3:
			if repre == 1:
				vert = int(input("Vertice escolhido:"))
				exc = grafo.eccentricity(u = vert)
				print("A excentricidade do vertice ", vert, " é ", exc)
				
			else:
				print("Algoritmo não implementado para esta representação")

		elif opcao == 4:
			if repre == 1:
				dia = grafo.Diameter()
				print("O diametro do grafo é ", dia)
				
			else:
				print("Algoritmo não implementado para esta representação")

		elif opcao == 5:
			if repre == 1:
				r = grafo.Radius()
				print("O raio do grafo é ", r)
				
			else:
				print("Algoritmo não implementado para esta representação")

		elif opcao == 6:
			if repre == 1:
				orig = int(input("Vertice de origem:"))
				grafo.Prim(u = orig)
				print("MST do grafo por Prim, iniciando pelo vertice ", orig)
				print(grafo.MTS)
				
			else:
				print("Algoritmo não implementado para esta representação")


		elif opcao == 7:
			if repre == 1:
				grafo.Kruskal()
				print("MST do grafo por Kruskal ")
				print(grafo.MTS)
				
			else:
				print("Algoritmo não implementado para esta representação")

		elif opcao == 8:
			if repre == 1:
				orig = int(input("Vertice de origem:"))
				dist = float(input("Distancia maxima:"))
				result = grafo.DistMenor(orig, dist)
				if len(result) > 0:
					print("Os vertices com distancia menor que",dist,"do vertice",orig,"são:")
					print(result)
				else:
					print("Não há vertices dentro da distancia escolhida")
			else:
				print("Algoritmo não implementado para esta representação")

		








