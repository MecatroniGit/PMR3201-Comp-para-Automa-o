"""
EP1 PMR3201(Computação para Automação)

@author: Júlia Mello de Almeida
NUSP: 11258082

"""

import pandas as pd 
import nltk as nk 
nk.download('stopwords')
import matplotlib.pyplot as plt 
import wordcloud as wd 
from nltk.corpus import stopwords
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

##Leitura do arquivo *.txt
 
def gerador_de_grafico(texto):
        
    f = open(texto,"r", encoding="utf-8-sig") # Abre o arquivo
    raw = f.read() # Le o conteudo do arquivo 
        
    ##Realiza pré-processamento que resulta na lista de strings <words_ns> 
    
    # Cria um tokenizer que mantem somente palavras 
    tokenizer = nk.tokenize.RegexpTokenizer("\w+")
    tokens = tokenizer.tokenize(raw) 
    # A variavel tokens e’ uma lista de tokens 
    # transformando todos os tokens em letras minusculas 
    lwords = [] 
    
    for word in tokens:
        lwords.append(word.lower())
    # lwords agora so contem tokens com letras minusculas
    # carrega as stopwords da lingua Inglesa em sw 
    sw = nk.corpus.stopwords.words("english")
    words_ns = [] 
    for word in lwords: 
        if word not in sw: words_ns.append(word) 
    # word_ns contem tokens sem stopwords
        
    ##Inicialize o dicionario <dicfreq> que contem pares (<x>,<nocorrer>)
    
    dicfreq = {"a":{}, "b":{}, "c":{}, "d":{}, "e":{}, "f":{}, "g":{}, "h":{}, "i":{}, "j":{}, "k":{}, "l":{}, "m":{}, 'n':{} , 'o':{}, 'p':{}, 'q':{}, 'r':{}, 's':{}, 't':{}, 'u':{}, 'v':{}, 'w':{}, 'x':{}, 'y':{}, 'z':{}}
    alfabetolw = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] 
    #Para cada string <x> na lista <words_ns> faça: 
        
    
    for word in words_ns:
        lista = list(word)
        x = lista[0]
        if (x in alfabetolw):
            if word in dicfreq[x]: 
                #Se <x> se encontra em <dicfreq>: 
                 #Atualizar o par (<x>,<n_ocorrer>) em <dicfreq>
                count=dicfreq[x][word] 
                count=count+1 #Então <n_ocorrer> = <nocorrer> + 1
                dicfreq[x][word]=count 
                
            else:         
                dicfreq[x].update([(word,1)]) 

        
         
    #Para cada par (<x>,<nocorrer>) de <dicfreq> inserir em uma lista ordenada <lwocorrencias> 
    #Os elementos devem ser lidos de <dicfreq> e inseridos na lista <lwocorrencias> 
    #numa ordem decrescente quando considerando <nocorr>. 
    # Nessa lista os elementos devem estar ordenados em ordem decrescente do número 
    # de ocorrências <nocorrer> 
    
    def insertionSort(arranjo):
    
        for i in range(1, len(arranjo)): #do segundo item até o ultimo
            elementonovo = arranjo[i] #compara tuplas com o primeiro
            j = i - 1 #indice do elemento comparativo        
            while j >= 0 and elementonovo[1] > arranjo[j][1]: 
                arranjo[j + 1] = arranjo[j]            
                j = j - 1
    
            arranjo[j + 1]= elementonovo  
            
            
    lwocorrencias = []
    for letras in dicfreq:
        for key in dicfreq[letras]:
            value=dicfreq[letras][key]
            tuplas = (key,value)
            lwocorrencias.append(tuplas)
    
    
    insertionSort(lwocorrencias)
    
            
    freqdist = lwocorrencias[0:20]
    freqdistwc=dict(freqdist)
    
    #Gerar o gráfico de barras indicando as 20 palavras de maior ocorrência 
    
    freqword=pd.DataFrame.from_records(freqdist,columns=["word","count"])
    freqword.plot(kind="bar",x="word")
    
    #Gerar o gráfico wordcloud com as 20 palavras de maior ocorrência
    
    wordc = wd.WordCloud(width=900,height=500, max_words=20,\
    relative_scaling=1,normalize_plurals=False).generate_from_frequencies(freqdistwc)
    plt.figure();
    plt.imshow(wordc, interpolation="bilinear");
    plt.axis("off")
    plt.show()

gerador_de_grafico("AliceInWonderland.txt")
gerador_de_grafico("ThroughTheLookingGlass.txt")
gerador_de_grafico("WarAndPeace.txt")
