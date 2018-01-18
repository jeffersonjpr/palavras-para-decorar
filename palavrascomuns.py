#palavras para memorizar
import pickle
arq = open('dicionario.pck','rb')
dicio = pickle.load(arq)
arq.close()
print("Digite sucodeuva para parar")
while True:
    b= str(input("Digite a palavra: "))
    if b == 'sucodeuva':
        break
    if b not in dicio:
        print('A palavra %s nunca foi vista!Adicionada ao programa.'%b)
        dicio[b] = 1
    else:
        if dicio[b] >= 3:
            print("A palavra %s ja foi vista %i° vezes,adicione no anki!!"%(b,dicio[b]))
            dicio[b]+=1
        else:
            print("A palavra ja foi vista mas ainda nao atingiu os pontos necessarios")
            dicio[b]+=1
arq = open('dicionario.pck','wb')
pickle.dump(dicio,arq)
arq.close()
