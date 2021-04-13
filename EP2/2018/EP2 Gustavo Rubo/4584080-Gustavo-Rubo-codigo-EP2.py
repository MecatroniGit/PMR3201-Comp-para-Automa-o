"""
Nome: Gustavo Marangoni Rubo
NUSP: 4584080
"""

import numpy as np
import math
import re
import time

def main():
    nome_arquivo = input('Nome do arquivo: ')
    #nome_arquivo = "brasil.txt"
    arquivo_saida = "saida_EP2.txt"

    g = Grafo(nome_arquivo)

    casos = [['A', 'Y'], ['G', 'Y'], ['D', 'U'], ['Q', 'J'],
             ['V', 'K'], ['L', 'H'], ['T', 'W'], ['X', 'K']]
    #casos = [['X', 'K']]

    fp = open(arquivo_saida, "w")
	
    for c in casos:
        print(c[0], ' - ', c[1], ':', file=fp)
        print(c[0], ' - ', c[1], ':')
        d, path = g.AchaMenorCaminho(c[0], c[1])
        print("Caminho: ", path, file=fp)
        print("Caminho: ", path)
        print("Distância: ", d, file=fp)
        print("Distância: ", d)
        print("", file=fp)
        print("")

class Grafo:
    
	#Construtor:
    def __init__(self, nome_arquivo):

        self.graph = {}

        entrada = open(nome_arquivo, 'r')

        lin = entrada.readline()
        while(lin != ""):
            lin = lin.split()
            
            self.AcrescentaVertice(lin[0][0])

            for a in range(1, len(lin)):
                arg = lin[a].split(":")
                self.graph[lin[0][0]][arg[0]] = int(arg[1])
            
            lin = entrada.readline()

    def AcrescentaVertice(self, v):
        self.graph[v] = {}

    def RemoveVertice(self, v):
        if (self.graph[v] == {}):
            del self.graph[v]

    def AcrescentaArco(self, v1, v2, d):
        self.graph[v1][v2] = d
        self.graph[v2][v1] = d
        
    def RemoveArco(self, v1, v2):
        del self.graph[v1][v2]
        del self.graph[v2][v1]

    def AchaMenorCaminho(self, v1, v2):
        Path = []

		#declarando os vetores e dicionários de controle
        fila = []
        dist = {}
        visitado = {}
		
        #inicializando o grafo
        for v in self.graph:
            visitado[v] = False
            dist[v] = math.inf

        fila.append(v1)
        dist[v1] = 0

		#visitando todos os vértices na fila
        for v in fila:
            visitado[v] = True
            for vv in self.graph[v]:
                if not (visitado[vv]):
                    fila.append(vv)
                if (dist[vv] > dist[v] + self.graph[v][vv]):
                    dist[vv] = dist[v] + self.graph[v][vv]

        v = v2
        Path.append(v)

		#determinando o caminho percorrido
        while(v != v1):
            min = list(self.graph[v].keys())[0]
            for vv in self.graph[v]:
                if (dist[vv] + self.graph[v][vv] <= dist[min] + self.graph[v][min]):
                    min = vv
            v = min
            Path.append(v)

        Path.reverse()
        
        return dist[v2], Path

    def ImprimeGrafo(self):
        for i in self.graph:
            print(i, " ->")
            for j in self.graph[i]:
                print(" ", j, ":", self.graph[i][j])

main()
