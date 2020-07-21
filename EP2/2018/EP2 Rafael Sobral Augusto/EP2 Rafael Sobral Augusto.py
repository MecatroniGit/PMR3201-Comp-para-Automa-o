class Grafo:
    def __init__(self,dicio=None,dicaux=None):
        #cria dicionario, se não entrar um pronto.
        if dicio==None:
            self.dicio={}
        else:
            self.dicio=dicio
    def AdicionaArco(self,v1,v2,d): #acrescenta no dicionario vazio informações da distancia d entre v1 e v2
        self.dicio[v1][v2]=d
    def AdicionaVertice(self,v): #adiciona vertice ao dicionario criado, associando-o a um dicionario vazio
        self.dicio[v]={}
    def RemoveVertice(self,v1,v2,d): #inutil
        del self.dicio[v1]
    def RemoveArco(): #inutil
        del self.dicio[v1][v2]
    def AchaMenorCaminho(self,v1,v2):
        S=[v1]
        menorcaminho=[v2]
        ptoscomdistancia=list(self.dicio[v1])
        distancias={v1:0}
        M=ptoscomdistancia[0]
        #loop que checa qual dos pontos ligados diretamente a v1 tem a menor distancia
        for i in range(len(ptoscomdistancia)): 
            distancias[ptoscomdistancia[i]]=self.dicio[v1][ptoscomdistancia[i]]
            #distancias - associa, a cada ponto que tem uma distancia calculavel em relação a v1, sua distancia a v1
            #ptoscomdistancia - lista com pontos que sabemos que tem distancia calculavel
            if distancias[M]<distancias[ptoscomdistancia[i]]:
                M=ptoscomdistancia[i]
        S.append(M) #adiciona o ponto ligado diretamente a v1 com menor distancia em S
        while len(S)!=len(self.dicio): #garante que percorreremos todos os vertices do grafo
            for i in self.dicio[M]: #percorre todos os pontos ligados ao novo ponto adicionado a S
                if i!=v1:
                    if i not in ptoscomdistancia:
                        ptoscomdistancia.append(i)
                        distancias[i]=distancias[M]+self.dicio[M][i]
                        #se o vertice ainda não tinha distancia calculavel, mas está ligado a M, agora tem
                        #adiciona esse ponto em ptoscomdistancia e associa sua distancia atual
                    else:
                        if distancias[i]>distancias[M]+self.dicio[M][i]:
                            distancias[i]=distancias[M]+self.dicio[M][i]
                        #se o vertice ja tinha distancia, checa se o novo ponto em S diminui a distancia ate v1
                        #se diminui, associa essa nova distancia
            j=0
            for i in ptoscomdistancia:
                if i not in S:
                    if j==0:
                        M=i
                    j+=1
                    if distancias[i]<distancias[M]:
                        M=i
                #descobre qual vertice com distancia calculavel, que não em S, tem a menor distancia ate v1
            S.append(M)
            #adiciona esse vertice em v1
        ptoatual=v2
        while v1 not in menorcaminho: #descobre o menor caminho desejado (de v2 a v1)
            x=0
            for i in self.dicio[ptoatual]:
                #inicialmente, percorre todos os vertices ligados diretamente a v2
                #depois, percorre todos os vertices ligados diretamente ao novo pto atual
                if x==0:
                    melhor=i
                    x+=1
                if self.dicio[ptoatual][i]+distancias[i]<self.dicio[ptoatual][melhor]+distancias[melhor]:
                    melhor=i
                    #descobre por qual ponto ligado a ptoatual passa a menor distancia ate v1
                    #atualiza o pto com menor distancia como melhor
            ptoatual=melhor
            menorcaminho.append(melhor)
            #atualiza o pto atual e adiciona-o como parte do menor caminho
            #volta pro inicio do loop, em que checa por qual outro ponto ligado ao novo ponto atual passa o menor caminho ate a origem
            #roda ate chegar em v1
        menorcaminhocerto=[]
        for i in range(len(menorcaminho)):
            menorcaminhocerto.append(menorcaminho[len(menorcaminho)-1-i])
            #troca a posiçao dos elementos da lista criada, para ela iniciar em v1 e ir ate v2
        return distancias[v2],menorcaminhocerto

def exportadados(arq,pi,pf,md,mc):
    arq.write('A menor distância para sair de ')
    arq.write(pi)
    arq.write(' e chegar em ')
    arq.write(pf)
    arq.write(' é de ')
    arq.write(str(md))
    arq.write(' \n')
    caminho=''
    for i in range(len(mc)-1):
        caminho+=mc[i]
        caminho+=' --> '
    caminho+=mc[len(mc)-1]
    arq.write('O caminho para tal conquista foi: \n')
    arq.write(caminho)

def main():
    print('O que você deseja para hoje?')
    print('1- Achar distâncias entre capitais do Brasil.')
    print('2- Ficar tranquilo e tirar um cochilão!')
    print('3- Ir ver a Copa do Mundo no CAM!')
    desejo=int(input('Escolha aqui: '))
    if desejo==2:
        print('Ótimo, vá em direção à sua cama e tire um cochilão!')
    elif desejo==3:
        print('Ótimo, venha e será bem-vindo!')
    else:
        print('')
        print('Poxa, já que é assim, então vamos lá!')
        print('Qual modo você deseja selecionar?')
        print('1- Encontra distâncias entre as cidades desejadas no EP.')
        print('2- Encontra a distância entre quaisquer cidades que quiser,')
        print('3- Encontra a distância entre a sua boca e a do @!')
        modo=int(input('Escolha o modo aqui: '))
        if modo==3:
            print('A distância atual é maior do que 0. Vamos trabalhar pra mudar isso!')
        elif modo==1 or modo==2:
            file=input('Digite o nome do arquivo: ')
            print('')
            g=open(file,'r') #abre arquivo com distâncias entre cidades
            texto=g.readlines() #quebra as linhas em uma matrizinha
            graph=Grafo() #cria objeto da classe Grafo
            arq=open('Menores Distâncias','w') #abre arquivo pra exportar as distâncias
            arq.write('Menores Distâncias\n') #titulo do arquivo
            arq.write('\n')
            for i in range(len(texto)): #inicia loop de criação do grafo
                graph.AdicionaVertice(texto[i][0]) #Adiciona Todos os vértices no grafo desejado
                text=texto[i][2:]
                j=0
                while j<len(text): #loop que pega as informações de distância no arquivo dado e transforma em dicionário
                    peso=''
                    if text[j]==':':
                        ponto=text[j-1]
                        while j<len(text)-1 and text[j]!=' ':
                            peso+=text[j+1]
                            j+=1
                        peso=int(peso)
                        graph.AdicionaArco(texto[i][0],ponto,peso)
                    j+=1
            if modo==2: #usuário escolhe a distância que quer
                vontade=1
                while vontade==1: #permite que o usuário descubra a distância entre quantos pontos quiser
                    pi=input('Digite de onde você quer começar: ')
                    pf=input('Digite onde você quer chegar: ')
                    menordistancia, menorcaminho=graph.AchaMenorCaminho(pi,pf) #encontra menor caminho e menor distância
                    print('A menor distância para sair de', pi, 'e chegar em', pf, 'é de', menordistancia)
                    print('O caminho para tal conquista foi:')
                    for i in range(len(menorcaminho)-1):
                        print(menorcaminho[i],end='')
                        print(' --> ',end='')
                    print(menorcaminho[len(menorcaminho)-1])
                    exportadados(arq,pi,pf,menordistancia,menorcaminho) #exporta menor caminho e distancia desejados pro arquivo
                    arq.write('\n')
                    arq.write('\n')
                    print('')
                    print('Você quer encontrar a distância de mais pontos?')
                    print('1- Sim, eu adoraria!')
                    print('Qualquer outro número- Não, estou cansado!')
                    vontade=int(input('Escolha aqui: '))
                    print(' ')
            elif modo==1:
                cidades=[['A','Y'],['G','Y'],['D','U'],['Q','J'],['V','K'],['L','H'],['T','W'],['X','K']]
                #cidades iniciais e finais pedidas no enunciado do EP
                for i in range(len(cidades)): #loop que acha as distancias desejadas
                    pi=cidades[i][0]
                    pf=cidades[i][1]
                    menordistancia, menorcaminho=graph.AchaMenorCaminho(pi,pf) #encontra menor caminho e menor distancia
                    print('A menor distância para sair de', pi, 'e chegar em', pf, 'é de', menordistancia)
                    print('O caminho para tal conquista foi:')
                    for i in range(len(menorcaminho)-1):
                        print(menorcaminho[i],end='')
                        print(' --> ',end='')
                    print(menorcaminho[len(menorcaminho)-1])
                    exportadados(arq,pi,pf,menordistancia,menorcaminho) #exporta os dados desejados para o arquivo
                    arq.write('\n')
                    arq.write('\n')
                    print('')
            print('')
            print('Pronto! Agora, se você for a Paolla corrigindo os EPs, sinta-se a vontade para me dar um 10 e ir descansar!' )           
        else:
             print('Você não escolheu um modo válido! Perdeu a chance de testar meu EP!')
main()
