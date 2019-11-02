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









