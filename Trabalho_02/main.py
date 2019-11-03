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


	primeiroData = readAchive(primeiro_arquivo)
	segundoData = readAchive(segundo_arquivo)

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




	
