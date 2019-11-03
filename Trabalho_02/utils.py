from tree import BTree
from avl import AvlTree
from redblack import RedBlack
from hash import HashTable
from list import List 

def readAchive(arq):
	file = open(arq, "r")
	string = file.read()
	string = string.replace('[', '')
	string = string.replace(']', '')
	lista = string.split(", ")
	listNum = []
	for item in lista:
		listNum.append(int(item))

	return listNum


def loadLista(lista):
	if not lista is None:
		MyList = List()
		for item in lista:
			MyList.append(item)

		return MyList
	return None


def loadHash(lista):
	if not lista is None:
		MyHash = HashTable()
		for item in lista:
			MyHash.insert(item,item)

		return MyHash

	return None


def loadBtree(lista):
	if not lista is None:
		MyTree = BTree()
		for item in lista:
			MyTree.insert(item)

		return MyTree
	return None


def loadAVL(lista):
	if not lista is None:
		MyAVL = AvlTree()
		for item in lista:
			MyAVL.insert(item)

		return MyAVL
	return None


def loadRedBlack(lista):
	if not lista is None:
		MyRB = RedBlack()
		for item in lista:
			MyRB.insert(item)

		return MyRB
	return None


#OP1 elementos de A que estão em B
#OP2 Inserir em B, os elementos de A que Não estão em B
#OP3 Remover os elementos de A que estão em B

def OP1List(lista1, lista2):
	if not (lista1 is None or lista2 is None):
		inter = []
		for item in lista1:
			aux = lista2.get(item)
			if aux == item:
				inter.append(item)
		return inter


def OP1Hash(lista, Hash):
	if not (lista is None or Hash is None):
		inter = []
		for item in lista:
			aux = Hash.get(item)
			if aux == item:
				inter.append(item)
		return inter

def OP1BTree(lista, BTree):
	if not (lista is None or BTree is None):
		inter = []
		for item in lista:
			aux = BTree.get(item)
			if aux == item:
				inter.append(item)
		return inter



def OP1AVL(lista, AVL):
	if not (lista is None or AVL is None):
		inter = []
		for item in lista:
			aux = AVL.get(item)
			if aux == item:
				inter.append(item)
		return inter


def OP1RB(lista, RB):
	if not (lista is None or RB is None):
		inter = []
		for item in lista:
			aux = RB.get(item)
			if aux == item:
				inter.append(item)
		return inter


def OP1(est1, est2, Name):
	if Name == "lista":
		est2 = loadLista(est2)
		l = OP1List(est1, est2)
	elif Name == "hash":
		est2 = loadHash(est2)
		l = OP1Hash(est1, est2)
	elif Name == "binary_tree":
		est2 = loadBtree(est2)
		l = OP1BTree(est1, est2)
	elif Name == "avl":
		est2 = loadAVL(est2)
		l = OP1AVL(est1, est2)
	elif Name == "red_black":
		est2 = loadRedBlack(est2)
		l = OP1RB(est1, est2)

	if l != None:
		return str(l)


#OP2 Inserir em B, os elementos de A que Não estão em B


def OP2List(lista1, lista2):
	if not (lista1 is None or lista2 is None):
		for item in lista1:
			aux = lista2.get(item)
			if aux == None:
				lista2.append(item)
		


def OP2Hash(lista, Hash):
	if not (lista is None or Hash is None):
		for item in lista:
			aux = Hash.get(item)
			if aux == None:
				Hash.insert(item)
		

def OP2BTree(lista, BTree):
	if not (lista is None or BTree is None):
		for item in lista:
			aux = BTree.get(item)
			if aux == None:
				BTree.insert(item)
		



def OP2AVL(lista, AVL):
	if not (lista is None or AVL is None):
		for item in lista:
			aux = AVL.get(item)
			if aux == None:
				AVL.insert(item)
		


def OP2RB(lista, RB):
	if not (lista is None or RB is None):
		for item in lista:
			aux = RB.get(item)
			if aux == None:
				RB.insert(item)
		

















