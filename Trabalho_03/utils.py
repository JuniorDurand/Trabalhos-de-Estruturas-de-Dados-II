from Graph_list import Graph as Graph_ls
from Graph_matrix import Graph as Graph_mx
import heapq
import sys


def readGraphList(arq, orient):
	arq = open(arq, 'r')
	grafo = None
	if not arq is None:
		texto = arq.readlines()
		size = int(texto[0])
		grafo = Graph_ls(size, oriented = orient)
		for linha in texto[1:]:
		    args = linha.split(" ")
		    if len(args) == 3:
		    	grafo.addEDGE(int(args[0]),int(args[1]),weight= float(args[2]))
		    else:
		    	grafo.addEDGE(int(args[0]),int(args[1]))

	arq.close()
	return grafo


def readGraphMatrix(arq, orient):
	arq = open(arq, 'r')
	grafo = None
	if not arq is None:
		texto = arq.readlines()
		size = int(texto[0])
		grafo = Graph_mx(size, oriented = orient)
		for linha in texto[1:]:
		    args = linha.split(" ")
		    if len(args) == 3:
		    	grafo.addEDGE(int(args[0]),int(args[1]),weight= float(args[2]))
		    else:
		    	grafo.addEDGE(int(args[0]),int(args[1]))

	arq.close()
	return grafo
