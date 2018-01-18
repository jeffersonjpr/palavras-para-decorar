#palavras populares
import pickle
import os
arq = open('dicionario.pck','rb')
dicio = pickle.load(arq)
arq.close()
def litado():
    lista = []
    for key,value in sorted(dict.items(dicio)):
        lista.append('%-15s %s'%(key,value))
    while lista != []:
        print(' | ',end = '')
        for i in range(3):
            try:
                print(lista[i], end=' | ')
            except:
                pass
        print('\n')
        for i in range(3):
            try:
                del lista[0]
            except:
                pass
def save():
    arq = open('dicionario.pck','wb')
    pickle.dump(dicio,arq)
    arq.close()
while True:
    print()
    print("Digite sucodeuva para parar")
    print("Digite listado para listar")
    b= str(input("Digite a palavra: ")).lower()
    b = b.replace(' ','')
    os.system('CLS')
    while b == '':
        os.system('CLS')
        print('Palavra invalida!!')
        print("Digite sucodeuva para parar")
        print("Digite listado para listar")
        b= str(input("Digite a palavra: ")).lower()
        b = b.replace(' ','')
        os.system('CLS')
    if b == 'sucodeuva':
        break
    if b == 'listado':
        litado()
        continue
    if b not in dicio:
        print('A palavra \"%s\" nunca foi vista!Adicionada ao programa.'%b)
        dicio[b] = 1
    else:
        if dicio[b] >= 3:
            print("A palavra \"%s\" ja foi vista %i vezes,adicione no anki!!"%(b,dicio[b]))
            dicio[b]+=1
        else:
            print("A palavra \"%s\" ja foi vista porem ainda nao atingiu os pontos necessarios." %b)
            dicio[b]+=1
    save()



