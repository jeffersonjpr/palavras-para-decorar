#palavras populares
import pickle
import os
arq = open('dicionario.pck','rb')
dicio = pickle.load(arq)
arq.close()
while True:
    print()
    print("Digite sucodeuva para parar")
    b= str(input("Digite a palavra: ")).lower()
    b = b.replace(' ','')
    os.system('CLS')
    print("Palavra:",b)
    while b == '':
        print('Palavra invalida!!')
        b= str(input("Digite a palavra: ")).lower()
        b = b.replace(' ','')
    if b == 'sucodeuva':
        break
    if b not in dicio:
        print('A palavra %s nunca foi vista!Adicionada ao programa.'%b)
        dicio[b] = 1
    else:
        if dicio[b] >= 3:
            print("A palavra %s ja foi vista %i vezes,adicione no anki!!"%(b,dicio[b]))
            dicio[b]+=1
        else:
            print("A palavra ja foi vista porem ainda nao atingiu os pontos necessarios.")
            dicio[b]+=1
    arq = open('dicionario.pck','wb')
    pickle.dump(dicio,arq)
    arq.close()

