#mudar a ordem dos jogadores
'''lista = [0,1,2,3,4]
for i in range(len(lista)):
    val = lista[i]
    del lista[i]
    lista.append(val)

class Jogador():
    def __init__(self, nome, valor_mao):
        self.nome = nome
        self.valor_mao = valor_mao

lista_vencedores = []
for i in range(1):
    nome = input("nome: ")
    valor_mao = [int(input("valor_mao")), [int(item) for item in input("cartas").split()]]
    lista_vencedores.append(Jogador(nome, lista_vencedores))
    print(valor_mao)

x = lista_vencedores[0].valor_mao[0]
maos_iguais = 1
for i in range(1, len(lista_vencedores)):
    if lista_vencedores[i].valor_mao[0] == x:
        maos_iguais += 1
if maos_iguais > 1:
    for i in range(maos_iguais):
        for cont in range(maos_iguais):
            x = lista_vencedores[i].valor_mao[1][0]
            y = lista_vencedores[cont].valor_mao[1][0] 
            if x >= y:  
                val = lista_vencedores[i]
                lista_vencedores[i] = lista_vencedores[cont]
                lista_vencedores[cont] = val
x = lista_vencedores.valor_mao[1][0]
cartas_iguais = 1
for i in range(1, maos_iguais):
    if lista_vencedores[i].valor_mao[1][0] == x:
        cartas_iguais += 1
if cartas_iguais > 1:
    for i in range(maos_iguais):
        for cont in range(maos_iguais):
            x = lista_vencedores[i].valor_mao[1][1]
            y = lista_vencedores[cont].valor_mao[1][1] 
            if x >= y:  
                val = lista_vencedores[i]
                lista_vencedores[i] = lista_vencedores[cont]
                lista_vencedores[cont] = val

print(lista_vencedores[0].nome)
print("aquoi")