"""
Nome: Gustavo Marangoni Rubo
NUSP: 4584080
"""

import numpy as np
import re
import time

def main():
    nome_arquivo = input('Nome do arquivo: ')
    #nome_arquivo = 'Dados/Simple/teste_meu.cnf'
    #nome_arquivo = 'Dados/Uf20/uf20-05.cnf'
    #nome_arquivo = 'Dados/Uf50/uf50-01.cnf'

    try:
        formula, nbvar = ler(nome_arquivo)
    except:
        print('Falha na leitura do arquivo')

    opcao = int(input('Digite 1 para força bruta, 2 para aleatório: '))
    
    if (opcao == 1):
        solucao, i, tempo = BruteForce(formula, nbvar)
    elif (opcao == 2):
        solucao, i, tempo = RandomSearch(formula, nbvar)

    print('Quantidade de iterações: ', i)
    print('Solução: \n', solucao)
    print('Tempo: ', tempo, 's')
    #print('Tempo / iteração: ', 100000 * (fim - inicio) / (i + 1), ' * 10e-6 s')

#Lê o arquivo e retorna um objeto representando a fórmula
def ler(nome_arquivo):
    #Abrir o arquivo:
    entrada = open(nome_arquivo, 'r')

    #Pular as linhas de comentários:
    lin = entrada.readline()
    while (lin[0] == 'c'):
        lin = entrada.readline()

    #Extrair os números de variáveis e cláusulas    
    lin = re.sub(' +', ' ', lin.strip()).split(' ')
    nbvar, nbclauses = int(lin[2]), int(lin[3])
    formula = [[0 for i in range(3)] for j in range(nbclauses)]
    
    #Construir o objeto "formula"
    for i in range(0, nbclauses):
        lin = re.sub(' +', ' ', entrada.readline().strip()).split(' ')
        formula[i][0] = int(lin[0])
        formula[i][1] = int(lin[1])
        formula[i][2] = int(lin[2])
    
    entrada.close()
    return formula, nbvar
    
#Verifica se a solucao é válida, e retorna verdadeiro ou falso
def verificar_solucao(formula, solucao1, nbvar):

    #Criar uma nova solução com um "espelho" para que
    #os índices negativos sejam naturalmente negações
    solucao2 = [0] * ((nbvar * 2) + 1)
    for k in range (0, nbvar):
        solucao2[nbvar + 1 + k] = solucao1[k]
        solucao2[nbvar - 1 - k] = 1 - solucao1[k]

    #Lógica para conferir
    for i in range(0, len(formula)):
        if (not(solucao2[formula[i][0] + nbvar] or
                         solucao2[formula[i][1] + nbvar] or
                                  solucao2[formula[i][2] + nbvar])):
              return 0
    return 1

#Testa soluções em sequência até encontrar alguma
def BruteForce(formula, nbvar):
    inicio = time.time()
    
    i = 1
    sol = [0] * nbvar

    #O objeto da solução é construído com base
    #nos bits que representam o índice 'i'
    while (not verificar_solucao(formula, sol, nbvar)):
        sol = [(i >> j) % 2 for j in range (nbvar)]
        i += 1
    
    fim = time.time()

    return sol, i + 1, fim - inicio

#Testa soluções aleatórias até encontrar alguma
def RandomSearch(formula, nbvar):
    inicio = time.time()
    
    i = 0
    sol = RandomSolucao(nbvar)
    
    while (not verificar_solucao(formula, sol, nbvar)):
        sol = RandomSolucao(nbvar)
        i += 1
        
    fim = time.time()
    
    return sol, i + 1, fim - inicio

#Retorna uma solucao aleatória
#O código foi baseado naquele no enunciado do EP
def RandomSolucao(nbvar):
    a = np.random.randint(2, size=nbvar)
    return a.tolist()

main()
