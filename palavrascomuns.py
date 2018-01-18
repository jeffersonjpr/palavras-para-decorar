#palavras populares
import pickle
import os
invalido = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
arq = open('dicionario.pck','rb')
dicio = pickle.load(arq)
arq.close()
def litado():
    lista = []
    for key,value in sorted(dict.items(dicio)):
        lista.append('%-15s %s'%(key,value))
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
def save():
    arq = open('dicionario.pck','wb')
    pickle.dump(dicio,arq)
    arq.close()
while True:
    print("Digite 'sucodeuva' para parar")
    print("Digite 'listar' para listar")
    print("Digite 'deletar' para excluir uma palavra.")
    b= str(input("Digite a palavra: ")).lower()
    b = b.replace(' ','')
    for d in invalido:
        b = b.replace(d,'')
    os.system('CLS')
    while b == '':
        os.system('CLS')
        print('Palavra invalida!!')
        print("Digite 'sucodeuva' para parar")
        print("Digite 'listar' para listar")
        print("Digite 'deletar' para excluir uma palavra.")
        b= str(input("Digite a palavra: ")).lower()
        b = b.replace(' ','')
        os.system('CLS')
    if b == 'sucodeuva':
        break
    if b == 'listar':
        litado()
        continue
    if b == "deletar":
        litado()
        c = str(input("Digite a palavra que deseja deletar: ")).lower()
        try:
            os.system('CLS')
            del dicio[c]
            print('Palavra %s deletada com sucesso' %c)
            save()
        except:
            os.system('CLS')
            print('Palavra inexistente')
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



