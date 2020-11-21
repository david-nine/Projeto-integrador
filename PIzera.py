import random
from cacualr_mao import calcular_mao
'''
import time
time.clock() conta os segundos
'''
baralho = ["1p","1c","1e","1o","2p","2c","2e","2o","3p","3c","3e","3o","4p","4c","4e","4o","5p",
           "5c","5e","5o","6p","6c","6e","6o","7p","7c","7e","7o","8p","8c","8e","8o","9p","9c",
           "9e","9o","10p","10c","10e","10o","Jp","Jc","Je","Jo","Qp","Qc","Qe","Qo","Kp","Kc","Ke","Ko"]

class Jogador(object):
    def __init__(self, nome, cartas=[], dinheiro=1000):
        self.nome = nome
        self.cartas = cartas 
        self.dinheiro = dinheiro
        self.valor_mao = []
        self.aposta = 0
        self.win = False
    
    def apostar(self, aposta = 0, win = False, cobrir = False):
        if win == False and cobrir == False:
            while True:
                quantidade = int(input("valor: "))
                try:
                    quantidade = quantidade + aposta
                    if self.dinheiro >= quantidade:
                        self.dinheiro -= quantidade
                        start.dinheiro_mesa += quantidade
                        self.aposta = quantidade
                        start.aposta_rodada = quantidade
                    else:
                        raise ValueError("Não tem dinheiro brow")
                    break
                except ValueError as error:
                    print(error)
        elif win == True:
            self.dinheiro -= aposta
            start.dinheiro_mesa += aposta
            self.aposta = aposta
            start.aposta_rodada = aposta
        elif cobrir == True:
            if self.aposta == 0:
                self.dinheiro -= start.aposta_rodada
                start.dinheiro_mesa += start.aposta_rodada
                self.aposta = start.aposta_rodada
            else:
                self.dinheiro = self.dinheiro - (start.aposta_rodada - self.aposta)
                start.dinheiro_mesa += start.aposta_rodada
                self.aposta = start.aposta_rodada


    def jogar(self, mostrar):
        print("|===================================|")
        print("Vez de", self.nome)
        print("Dinheiro: ", self.dinheiro)
        print("Mesa:    ", mostrar)
        print("Sua mão: ", self.cartas)
        print("Aposta da rodada",start.aposta_rodada)
        print("|===================================|")
        print("O que deseja fazer?")
        dicionario = {"1": "1. apostar", "2": "2. passar", "3": "3. a win", "4": "4. cobrir", "5": "5. aumentar", "6": "6. correr"}
        if mostrar == "Rodada de apostas inicial": 
            if self.nome == start.rodada[0].nome:
                opcoes = ["1", "3", "6"]
            elif self.dinheiro > start.aposta_rodada:
                    opcoes = ["3", "4", "5", "6"]
            elif self.dinheiro == start.aposta_rodada:
                opcoes = ["3", "5", "6"]
            else:
                opcoes = ["3", "6"]
        else:
            if start.aposta_rodada == 0:
                opcoes = ["1", "2", "3", "6"]
            else:
                if self.dinheiro > start.aposta_rodada:
                    opcoes = ["3", "4", "5", "6"]
                elif self.dinheiro == start.aposta_rodada:
                    opcoes = ["3", "5", "6"]
                else:
                    print("aqui")
                    opcoes = ["3", "6"]
        for opcao in opcoes:
            print(dicionario[opcao])

        while True:
            jogada = input() 
            try:
                if "1" in opcoes and jogada == "1":
                    self.apostar()
                    if mostrar == "Rodada de apostas inicial" and self.nome == start.rodada[0].nome:
                        start.aposta_rodada *= 2
                elif "2" in opcoes and jogada == "2":
                    return True
                elif "3" in opcoes and jogada == "3":
                    self.apostar(self.dinheiro, win=True)
                    self.win = True
                elif "4" in opcoes and jogada == "4":
                    self.apostar(aposta=start.aposta_rodada, cobrir=True)
                elif "5" in opcoes and jogada == "5":
                    self.apostar(start.aposta_rodada)
                elif "6" in opcoes and jogada == "6":
                    self.correr()
                else:
                    raise ValueError("Jogada invalida!!")
                break
            except ValueError as error:
                print(error)
    
    def correr(self):
        for i in range(2):
            start.baralho.append(self.cartas[i])
        for jogador in start.rodada:
            if jogador.nome == self.nome:
                start.rodada.remove(jogador)
        self.cartas = []
        self.aposta = 0
            
    def receber(self, quantidade):
        self.dinheiro += quantidade

class Jogo(object):
    def __init__(self, baralho):
        self.jogadores = self.add_jogadores()
        self.baralho = baralho
        self.mesa = []
        self.dinheiro_mesa = 0
        self.rodada = []
        self.aposta_rodada = 0
        self.vencedor = None
    
    def dar_cartas(self):
        for i in range(len(self.jogadores)):
            cartas = [] 
            for cont in range(2):
                c = random.choice(self.baralho)
                self.baralho.remove(c)
                cartas.append(c)
            self.jogadores[i].cartas = cartas 
        for i in range(5):
            c = random.choice(baralho)
            self.baralho.remove(c)
            self.mesa.append(c)

    def add_jogadores(self):
        while True:
            try:
                num = int(input("Quantidade de jogadores?: "))
                if not 2 <= num <= 8:
                    raise ValueError("Quantidade fora do permitido")
                break
            except ValueError as error:
                print(error)    
        j = []
        for i in range(num):
            if len(j) >= 1:
                while True:
                    nome = input("Nome do jogador: ") 
                    try:
                        x = 0
                        for jogador in j:
                            if jogador.nome == nome:
                                x = 1
                        if x == 0:
                            print("aqui")
                            player = Jogador(nome)
                            j.append(player)
                        else:    
                            raise ValueError("Este nome já existe!! Tente outro.")
                        break
                    except ValueError as error:
                        print(error)  
            else:  
                nome = input("Nome do jogador: ") 
                player = Jogador(nome)
                j.append(player)
        return j


    def calcular_vencedor(self):
        for jogador in self.jogadores:
            jogador.valor_mao = calcular_mao(jogador.cartas, self.mesa)
            del self.mesa[6]
            del self.mesa[5]
        lista_vencedores = self.rodada
        for i in range(len(self.rodada)):
            for cont in range(len(self.rodada)):
                x = lista_vencedores[i].valor_mao[0]
                y = lista_vencedores[cont].valor_mao[0] 
                if x >= y:  
                    val = lista_vencedores[i]
                    lista_vencedores[i] = lista_vencedores[cont]
                    lista_vencedores[cont] = val
        x = lista_vencedores[0].valor_mao[0]
        maos_iguais = 1
        for i in range(1, len(lista_vencedores)):
            if lista_vencedores[i].valor_mao[0] == x:
                maos_iguais += 1
        if maos_iguais > 1:
            for n in range(2):
                for i in range(maos_iguais):
                    for cont in range(maos_iguais):
                        x = lista_vencedores[i].valor_mao[1][n]
                        y = lista_vencedores[cont].valor_mao[1][n] 
                        if x >= y:  
                            val = lista_vencedores[i]
                            lista_vencedores[i] = lista_vencedores[cont]
                            lista_vencedores[cont] = val
        x = lista_vencedores[0].valor_mao[1][0]
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
            
        if lista_vencedores[0].valor_mao == lista_vencedores[1].valor_mao:
            if lista_vencedores[1].valor_mao == lista_vencedores[2].valor_mao:
                if lista_vencedore[2].valor_mao == lista_vencedores[3].valor_mao:
                    for i in range(4):
                        lista_vencedores[i].receber(quantidade)
                else:
                    for i in range(3):
                        lista_vencedores[i].receber(quantidade)
            else:
                quantidade = self.dinheiro_mesa//2
                for i in range(2):
                    lista_vencedores[i].receber(quantidade)
        else:
            lista_vencedores[0].receber(self.dinheiro_mesa)
        self.vencedor = lista_vencedores[0]
        for jogador in lista_vencedores:
            jogador.correr()


    def rodadas(self):
        i = 0
        self.rodada = self.jogadores.copy()
        mostrar = [self.mesa[0], self.mesa[1], self.mesa[2]]
        while i < 4 and len(self.rodada) > 1: 
            for jogador in self.rodada:
                if i != 0:
                    jogador.jogar(mostrar)
                else:
                    jogador.jogar("Rodada de apostas inicial")
            if len(self.rodada) == 1:
                return self.calcular_vencedor()            
            for jogador in self.rodada:
                if self.aposta_rodada != jogador.aposta:
                    if i > 0:
                        jogador.jogar(mostrar)
                    else:
                        if jogador != self.rodada[0]:
                            jogador.jogar(mostrar)
            for jogador in self.rodada:
                if jogador.win == True:
                    return self.calcular_vencedor()
            for jogador in self.rodada:
                jogador.aposta = 0
            if i != 0 and i < 3:
                mostrar.append(self.mesa[i+2])
            self.aposta_rodada = 0
            i += 1
        self.calcular_vencedor()

    def reiniciar(self):
        self.dinheiro_mesa = 0
        val = self.jogadores[0]
        self.jogadores.remove(val)
        self.jogadores.append(val)
        for jogador in self.jogadores:
            if jogador.dinheiro == 0:
                print("Jogador", jogador.nome,", seu dinheiro acabou! Você foi removido da mesa")
                self.jogadores.remove(jogador)
        for i in range(5):
            self.baralho.append(self.mesa[i])
        self.mesa = []
        if len(self.jogadores) < 2:
            print("O jogo acabou!!", self.jogadores[0].nome," você venceu")
            print("Voce ganhou", self.jogadores[0].dinheiro," em fichas")
            return False


if __name__ == "__main__":
    start = Jogo(baralho) 
    while True: 
        start.dar_cartas()   
        start.rodadas()      
        print("Vencedor:", start.vencedor.nome)
        r = start.reiniciar()
        if r == False:
            break
        op = input("Desejam continuar ( s / n ): ")
        if op != "s":
            break