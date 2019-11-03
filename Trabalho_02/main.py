from tree import BTree
from avl import AvlTree
from redblack import RedBlack
from hash import HashTable
from list import List 


from utils import *

import argparse 
import time



if __name__ == "__main__":


	parser = argparse.ArgumentParser()

	#definindo primeiro arquivo de entrada
	parser.add_argument("primeiro_arquivo", type=str, help="Arquivo conjunto A")

	#definindo segundo arquivo de entrada
	parser.add_argument("segundo_arquivo", type=str, help="Arquivo conjunto B")

	#definindo TAD utilizado
	parser.add_argument("estrutura_dados", type=str, help="Estrutura de dados de B")

	#definindo operação
	parser.add_argument("operacao", type=int, help="Operação")
	

	#utilizar da seguinte forma:
	# "main.py [conjunto a] [conjunto b] [estrtura]"

	parser.add_argument('-v', '--verbose', action="store_true", default=False, help="imprime no final da execução dados do precedimento")

	args = parser.parse_args()

	primeiro_arquivo = args.primeiro_arquivo
	segundo_arquivo = args.segundo_arquivo
	estrutura_dados = args.estrutura_dados
	operacao = args.operacao

	

	print("Carregando primeiro arquivo")
	primeiroData = readAchive(primeiro_arquivo)
	if not primeiroData is None:
		print("primeiro arquivo carregado")
	else:
		print("primeiro não carregado")
		exit()

	

	print("Carregando segundo arquivo")
	segundoData = readAchive(segundo_arquivo)
	if not primeiroData is None:
		print("segundo arquivo carregado")
	else:
		print("segundo não carregado")
		exit()

	
	start = time.time()
	A = loadLista(primeiroData)
	if operacao == 1:

		result = OP1(A, segundoData, estrutura_dados)

		print("========")
		print(result)
		print("========")

	elif operacao == 2:

		result = OP2(A, segundoData, estrutura_dados)

		print("========")
		print(result)
		print("========")

	elif operacao == 3:

		result = OP3(A, segundoData, estrutura_dados)

		print("========")
		print(result)
		print("========")

	else:
		print("Operação invalida")
		exit()


	end = time.time()
	print("tempo de execução : ", end-start)



	
