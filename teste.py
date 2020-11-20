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


dicionario = {"1": "1. apostar", "2": "2. passar", "3": "3. a win", "4", "4. cobrir", "5": "5. aumentar", "6": "6.correr"}
if rodadainicial: 
    if jogador == jogadores[0]:
        opcoes = ["1", "3", "6"]
    else:  
        opcoes = ["3", "4", "5", "6"]
else:
    if aposta_rodada == 0:
        opcoes = ["1", "2", "3", "6"]
    else:
        if jogador.dinheiro >= aposta_rodada:
            opcoes = ["3", "4", "5", "6"]
        else:
            opcoes = ["3", "6"]
for opcao in opcoes:
    print(dicionario[opcao])

while True:
    jogada = input() 
    try:
        if "1. apostar" in opcoes and jogada == "1":
            self.apostar()
        elif "2. passar" in opcoes and jogada == "2":
            self.passar()
        elif "3. a win" in opcoes and jogada == "3":
            self.apostar(self.dinheiro, win=True)
        elif "4. cobrir" in opcoes and jogada == "4":
            self.apostar(aposta=start.aposta_rodada, cobrir=True)
        elif "5. aumentar" in opcoes and jogada == "5":
            self.apostar(start.aposta_rodada)
        elif "6. correr" in opcoes and jogada == "6":
            self.correr()
        else:
            raise ValueError("Jogada invalida!!")
    except ValueError as error:
        print error