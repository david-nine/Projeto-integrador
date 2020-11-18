#mudar a ordem dos jogadores
lista = [0,1,2,3,4]
for i in range(len(lista)):
    val = lista[i]
    del lista[i]
    lista.append(val)

#ordenar lista do vencedor
lista2 = [1,5,6,2,7]
lista2.sort()
lista2.reverse()