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
        self.aposta = None
        self.win = False

    def getJogador(self, nome):
        for jogador in start.jogadores:
            if jogador.nome == nome:
                return jogador 
    
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
            self.dinheiro -= start.aposta_rodada
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
        dicionario = {"1": "1. apostar", "2": "2. passar", "3": "3. a win", "4": "4. cobrir", "5": "5. aumentar", "6": "6.correr"}
        if mostrar == "Rodada de apostas inicial": 
            if self.nome == start.rodada[0].nome:
                opcoes = ["1", "3", "6"]
            else:  
                opcoes = ["3", "4", "5", "6"]
        else:
            if start.aposta_rodada == 0:
                opcoes = ["1", "2", "3", "6"]
            else:
                if self.dinheiro >= start.aposta_rodada:
                    opcoes = ["3", "4", "5", "6"]
                else:
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
        # if mostrar == "Rodada de apostas inicial":
        #     if self.nome != start.rodada[0].nome:
        #         print("1. Apostar")
        #         print("2. Cobrir")
        #         print("3. Correr")
        #         while True:
        #             jogada = input()
        #             try:
        #                 if jogada == '1':   
        #                     self.apostar()
        #                     start.aposta_rodada = quantidade * 2
        #                 elif jogada == '2':
        #                     self.apostar(aposta=start.aposta_rodada, cobrir=True)
        #                 elif jogada == '3':    
        #                     self.correr()
        #                 else:
        #                     raise ValueError("Jogada inválida")
        #                 break
        #             except ValueError as error:
        #                 print(error)
        #     else:
        #         print("1. Apostar")
        #         print("2. Correr")
        #         print("3. A win")
        #         while True:
        #             jogada = input()
        #             try:
        #                 if jogada == '1':
        #                     self.apostar()
        #                     start.aposta_rodada *= 2
        #                 elif jogada == '2':
        #                     self.correr()
        #                 elif jogada == '3':
        #                     self.apostar(aposta=self.dinheiro, win=True)
        #                     self.win = True
        #                 else:
        #                     raise ValueError("Jogada inválida")
        #                 break
        #             except ValueError as error:
        #                 print(error)

        # elif start.aposta_rodada == 0:
        #     print("1. Apostar")
        #     print("2. Passar")
        #     print("3. A win")
        #     print("4. Correr")
        #     while True:
        #         jogada = input() 
        #         try:
        #             if jogada == '1':
        #                 self.apostar()
        #             elif jogada == '2':
        #                 return True
        #             elif jogada == '3': 
        #                 self.apostar(aposta=self.dinheiro, win=True)
        #                 self.win = True
        #             elif jogada == '4':
        #                 self.correr()
        #             else:
        #                 raise ValueError("Jogada inválida")
        #             break
        #         except ValueError as error:
        #             print(error)
        # else:
        #     if self.dinheiro <= start.aposta_rodada:
        #         print("1. A win")
        #         print("2. Correr")
        #         while True:
        #             jogada = input()
        #             if jogada == '1': 
        #                 self.apostar(aposta=self.dinheiro, win=True)
        #                 self.win = True
        #             elif jogada == '2':
        #                 self.correr()
        #     else:
        #             print("1. Aumentar")
        #             print("2. Cobrir")
        #             print("3. A win")
        #             print("4. Correr")
        #             while True:
        #                 jogada = input()
        #                 try:
        #                     if jogada == '1':
        #                         self.apostar(aposta=start.aposta_rodada)
        #                     elif jogada == '2':
        #                         self.apostar(aposta=start.aposta_rodada, cobrir=True)
        #                     elif jogada == '3': 
        #                         self.apostar(aposta=self.dinheiro, win=True)
        #                         self.win = True
        #                     elif jogada == '4':
        #                         self.correr()
        #                     else:
        #                         raise ValueError("Jogada inválida")
        #                     break
        #                 except ValueError as error:
        #                     print(error)

    def correr(self):
        start.baralho
        for i in range(2):
            start.baralho.append(self.cartas[i])
        jogador = self.getJogador(self.nome)
        start.rodada.remove(jogador)
        self.cartas = []

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
        jogadores = []
        while True:
            try:
                num = int(input("Quantidade de jogadores?: "))
                if not 2 <= num <= 8:
                    raise ValueError("Quantidade fora do permitido")
                break
            except ValueError as error:
                print(error)    
        for i in range(num):
            nome = input("Nome do jogador: ")
            player = Jogador(nome)
            jogadores.append(player)
        return jogadores


    def calcular_vencedor(self):
        for jogador in self.jogadores:
            jogador.valor_mao = calcular_mao(jogador.cartas, self.mesa)
            del self.mesa[6]
            del self.mesa[5]
        # for i in range(2):
        #     for jogardor in self.rodada:
                

    def rodadas(self):
        i = 0
        self.rodada = self.jogadores
        mostrar = [self.mesa[0], self.mesa[1], self.mesa[2]]
        while i < 4 and len(self.rodada) > 1: 
            for jogador in self.rodada:
                print(self.rodada)
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
        return self.calcular_vencedor()
            
            # if len(self.rodada) == 1:
            #     receber(self.rodada[0])
            #     break

if __name__ == "__main__":
    start = Jogo(baralho) 
    start.dar_cartas()   
    start.calcular_vencedor()
    start.rodadas()      
    for j in start.jogadores:    
        a = start.jogadores[0]
        print(j.nome)
        print(j.cartas)
        print(j.valor_mao)
        print(j.dinheiro)
    print(start.mesa)