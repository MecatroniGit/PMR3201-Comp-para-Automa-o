from heapq import heappush, heappop

class Node:
    def __init__(self, car=None,freq=None,left=None,right=None):
        self.caracter = car
        self.frequencia = freq
        self.left = left
        self.right = right
    
    def __str__(self):
        if (self.caracter is None):
            return('0')
        else:
            return('1')
        
    def __lt__(self,other):
        if (self.frequencia <= other.frequencia):
            return(True)
        else:
            return(False)
            
class BST:
    def __init__(self,root=None):
        self.root = root
        
    def devolveroot(self):
        return self.root
    
    def preordertraverse(self,p):
        if(p is not None):
            if (p.caracter is not None):
                print(p,end='')
            else:
                print(p,end='')
                self.preordertraverse(p.left)
                self.preordertraverse(p.right)
            
def codifica(codigo,no,atual,esquerda,atravessamento):
    if no.caracter!=None:
        atravessamento.append(1)
        if esquerda:
            codigo[no.caracter]=atual+'0'
        else:
            codigo[no.caracter]=atual+'1'
        atravessamento.append(bin(ord(no.caracter)))
    else:
        atravessamento.append(0)
        if esquerda:
            codifica(codigo,no.left,atual+'0', True, atravessamento)
            codifica(codigo,no.right,atual+'0',False, atravessamento)
        else:
            codifica(codigo,no.left,atual+'1', True, atravessamento)
            codifica(codigo,no.right,atual+'1', False, atravessamento)

def exportabites(caracteres,numerobites,arvorelinear,msgcodigo):
    arq=open('codigo.huf','wb')
    caracteres=str(caracteres)
    i=0
    while i<len(caracteres):
        x=bin(ord(caracteres[i]))
        x=x[2:]
        while len(x)<8:
            x='0'+x
        x=int(x)
        arq.write(bytes(x))
    #não funciona também
    return

def lebites(arq):
    arquivo=open(arq,'rb')
    texto=arquivo.read()
    print(texto)
        
def criptografa(file):
    f=open(file,'r')
    texto=f.readlines()
    A=[] #lista de caracteres
    B=[] #lista com frequencias
    for i in range (len(texto)):
        for j in range(len(texto[i])):
            if texto[i][j] not in A:
                A.append(texto[i][j])
                B.append(1)
            else:
                for k in range (len(A)):
                    if A[k]==texto[i][j]:
                        B[k]+=1
    i=0
    while i <len(A):
        A[i]=Node(A[i],B[i])
        i+=1
    aux=[]
    i=0
    listaordenada=[]
    caracteres=0
    for i in range(len(A)):
        heappush(aux,A[i])
        caracteres+=1
    caracteres=str(caracteres)
    while len(caracteres)<3:
        caracteres='0'+caracteres
    while len(aux)!=1:
        x=heappop(aux)
        y=heappop(aux)
        heappush(aux,Node(None,x.frequencia+y.frequencia,x,y))
    arvore=BST(aux[0])
    raiz=arvore.devolveroot()
    x=arvore.preordertraverse(raiz)
    codigo={}
    atual=''
    esquerda=True
    atravessamento=[]
    codifica(codigo,raiz,atual,esquerda,atravessamento)
    for i in codigo:
        codigo[i]=codigo[i][1:]
    arvorelinear=''    
    for x in atravessamento:
        x=str(x)
        if len(x)>1:
            x=x[2:]
            x='0'+x
            while len(x)<8:
                x='0'+x
        arvorelinear+=x
    print(arvorelinear)
    msgcodigo=''
    for i in range(len(texto)):
        for j in range(len(texto[i])):
            msgcodigo+=codigo[texto[i][j]]
    numerobites=len(msgcodigo)
    exportabites(caracteres,numerobites,arvorelinear,msgcodigo)

def decriptografa(arq):
    #não consegui
    return
    
def main():
    file=input('Digite o nome do arquivo: ')
    desejo=input('O que você deseja fazer? 1-criptografar 2- decriptografar') #deveria ser a interface
    if desejo=='1':
        criptografa(file)
    elif desejo=='2':
        print('Desculpe Lolla, meu EP não faz isso!')
    else:
        print('Desculpe, não é um comando válido')
if __name__ == "__main__": main()
            
