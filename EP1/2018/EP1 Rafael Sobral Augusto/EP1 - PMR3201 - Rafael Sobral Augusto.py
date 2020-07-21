# -*- coding: utf-8 -*-
"""
Spyder Editor

Este é um arquivo de script temporário.
"""

import numpy as np
import time

def Testa(formula,a):
    teste=[]
    for i in range(len(formula[0])):
        teste.append(0)
    #codigobom
    i=0
    contador=0
    while i<len(formula):
        controle=i
        j=0
        while j <len(formula[0]):
            if formula[i][j]>0:
                teste[j]=a[formula[i][j]-1]
            else:
                if a[abs(formula[i][j])-1]==0:
                    teste[j]=1
                else:
                    teste[j]=0
            if teste[j]==1:
                j=len(formula[i])
                i+=1
            else:
                j+=1
        if controle==i:
            i=len(formula)
        else:
            contador+=1
    return (contador)        

def TransformaBinario(contprincipal, variaveis):
    a=[]
    for i in range(variaveis):
        a.append(0)
    x=bin(contprincipal)
    p=2
    y=[]
    while p<len(x):
        y.append(int(x[p]))
        p+=1
    for i in range(len(y)):
        a[len(a)-i-1]=y[len(y)-i-1]
    return a

def RandomSearch(formula, variaveis):
    f=False
    contprincipal=0
    while not f:
        a=np.random.randint(2,size=variaveis)
        a=a.tolist()
        contador=Testa(formula,a)
        if contador==len(formula):
            f=True
        contprincipal+=1
    return a, contprincipal

def BruteForce(formula, variaveis):
    f=False
    contprincipal=0
    x=1
    for i in range(variaveis):
       x*=2
    while not f and contprincipal<x:
        a=TransformaBinario(contprincipal, variaveis)
        contador=Testa(formula,a)
        if contador==len(formula):
            f=True
        contprincipal+=1
    if f:
        return a, contprincipal
    else:
        return []

def main():
    formula=input('Digite o nome do arquivo: ')
    f=open(formula,'r')
    texto=f.readlines()
    i=0
    formula=[]
    while i<len(texto):
        if 'p' in texto[i][0]:
            i+=1
            while i<len(texto):
                x=texto[i].split(' ')
                y=[]
                for j in range(len(x)):
                    if x[j]!='' and x[j]!='\n':
                        x[j]=int(x[j])
                        if x[j]!=0:
                            y.append(x[j])
                if y!=[]:
                    formula.append(y)
                i+=1
        i+=1
    variaveis=0
    for i in range(len(formula)):
        for j in range(len(formula[i])):
            if abs(formula[i][j])>variaveis:
                variaveis=abs(formula[i][j])
    Modo=input('Qual modo você deseja selecionar? a- RandomSearch b- BruteForce ')
    if Modo=='a':
        start=time.time()
        gaba=RandomSearch(formula, variaveis)
        end=time.time()
        print('Uma solução para o problema é o conjunto: ', gaba[0])
        print('O número de iterações necessárias para chegar na solução foi: ', gaba[1])
        print(end-start)
    if Modo=='b':
        start=time.time()
        gaba=BruteForce(formula, variaveis)
        end=time.time()
        if len(gaba)>0:
            print('Uma solução para o problema é o conjunto: ', gaba[0])
            print('O número de iterações necessárias para chegar na solução foi: ', gaba[1])
            print(end-start)
        else:
            print('Não existem valores que satisfazem essa fórmula!')
main()
