#palavras populares
import pickle
from os import system
import webbrowser
invalido = ' 1234567890!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
try: #verifica se é a primeira vez abrindo o programa
    arq = open('dicionario.pck','rb')
    arq.close()
except: # caso seja a primeira vez, cria o arquivo de dump
    arq = open('dicionario.pck','wb')
    dicio = {}
    recentee = []
    pickle.dump(dicio,arq)
    pickle.dump(recentee,arq)
    arq.close()

arq = open('dicionario.pck','rb')
dicio = pickle.load(arq)
recentee = pickle.load(arq)
arq.close()

def litado():
    lista = []
    for key,value in sorted(dict.items(dicio)):
        lista.append('%-13s %s'%(key,value))
    while lista != []:
        if len(lista) > 6:
            print("| %s | %s | %s | %s | %s | %s |"%(lista[0],lista[1],lista[2],lista[3],lista[4],lista[5]))
        else:
            print('| ',end = '')
            for ne in range(len(lista)):
                print(lista[ne], end=' | ')
            print('\n')
        for i in range(6):
            try:
                del lista[0]
            except:
                pass
def save(): #salva as mundanças no arquivo externo
    arq = open('dicionario.pck','wb')
    pickle.dump(dicio,arq)
    pickle.dump(recentee,arq)
    arq.close()
def commandos(): #lista de comandos do programa
    print("Digite 'sucodeuva' para parar")
    print("Digite 'listar' para listar")
    print("Digite 'deletar' para excluir uma palavra.")
    print("Digite 'recente' para listar as ultimas palavras adicionadas.")
    print("Digite 'pesquisar' para pesquisar uma palavra.") ##*
    
while True:
    commandos()
    b= str(input("Digite a palavra: ")).lower()
    for d in invalido:
        b = b.replace(d,'')
    system('CLS')
    while b == '':
        system('CLS')
        print('Palavra invalida!!')
        commandos()
        b= str(input("Digite a palavra: ")).lower()
        b = b.replace(' ','')
        system('CLS')
    if b == 'sucodeuva':
        break
    if b == 'listar':
        litado()
        continue
    if b == "deletar":
        litado()
        c = str(input("Digite a palavra que deseja deletar: ")).lower()
        
        try: #tenta deletar a palavra que o usuario digitou
            system('CLS')
            del dicio[c]
            print('Palavra %s deletada com sucesso' %c)
            save()
        except:
            system('CLS')
            print('Palavra inexistente')
        for i in range(len(recentee)): #avisa na lista recente que a palavra foi deletada
            if recentee[i] == c:
                recentee[i] = "%s (deletada)" %c
        save()
        continue
    
    if b == "recente": #printa as ultimas 5 palavras adicionadas
        system('CLS')
        for i in range(len(recentee)):
            print('%iº: %s' %(i+1,recentee[i]))
        continue
    if b == "pesquisar": # abre alguns sites com a palavra escolhida. Atualmente google tradutor, google imagens e dicionario merriam webster
        peq = str(input("Digite a palavra a ser pesquisada:"))
        ##webbrowser.get('mozilla') nao sei usar ainda
        webbrowser.open("https://translate.google.com.br/#en/pt/%s"%peq,0)
        webbrowser.open("https://www.google.com/search?tbm=isch&q=%s"%peq,0)
        webbrowser.open("https://www.merriam-webster.com/dictionary/%s"%peq,0)
        system('CLS')
        continue

    if len(recentee) > 4: #adicionando  
        del recentee[0]   #as
    recentee.append(b)    #5 ultimas

    
    if b not in dicio:
        print('A palavra \"%s\" nunca foi vista!Adicionada ao programa.'%b)
        dicio[b] = 1
    else:
        if dicio[b] >= 2:
            dicio[b]+=1
            print("A palavra \"%s\" ja foi vista %i vezes."%(b,dicio[b]))
            print("####################")
            print("#-ADICIONE-NO-ANKI-#")
            print("####################")


            while True: #veririficar se o usuario prestou atençao nas palavras pontuadas
                try:
                    confi = int(input('Atenção, palavra vista %i vezes! Digite "1" para continuar.' %dicio[b]))
                    if confi == 1:
                        system('CLS')
                        break
                except:
                    continue
        else:
            print("A palavra \"%s\" ja foi vista porem ainda nao atingiu os pontos necessarios." %b)
            dicio[b]+=1
    save()



