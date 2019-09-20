from grafo import Grafo
from algoritmosDeOrdenacao import *
from utils import *




'''
Implemente o algoritmo de ordenação no arquivo algoritmosDeOrdenacao.py
Instruções básicas de como fazer a implementação estão no arquivo algoritmosDeOrdenacao.py
'''

if __name__ == "__main__":

    #algoritimoDeOrdenacao = InsertionSort()
    algoritimoDeOrdenacao = Quicksort()
    arquivoJson = './grafos/7vertices.json'
    arquivoDeSaida = './arvores_geradas/mst7Vertice2.txt'

    grafo = Grafo()
    grafo.estabelecerAlgoritmoDeOrdencao(algoritimoDeOrdenacao)
    grafo.carregarGrafo(arquivoJson)

    arvoreGeradoraMinima =  grafo.executarKruskal() 
    SalvarArvoreGeradoraMinimaEmArquivo(arquivoDeSaida, arvoreGeradoraMinima)

