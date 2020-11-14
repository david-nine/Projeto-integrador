import random
from cacualr_mao import calcular_mao
'''
import time
time.clock() conta os segundos
'''
baralho = ["1p","1c","1e","1o","2p","2c","2e","2o","3p","3c","3e","3o","4p","4c","4e","4o","5p",
           "5c","5e","5o","6p","6c","6e","6o","7P","7c","7e","7o","8p","8c","8e","8o","9p","9c",
           "9e","9o","10p","10c","10e","10o","Jp","Jc","Je","Jo","Qp","Qc","Qe","Qo","Kp","Kc","Ke","Ko"]

class Jogador(object):
    def __init__(self, nome, cartas=[], dinheiro=1000):
        self.nome = nome
        self.cartas = cartas 
        self.dinheiro = dinheiro
        self.valor_mao = []

    def apostar(self, quantidade):
        if self.dinheiro >= quantidade:
            self.dinheiro -= quantidade
        else:
            return False

    def jogar(self):
        jogada = input("deseja apostar nesta rodada") 
        if jogada == "s":
            quantidade = int(input("quantidade: "))    
            self.apostar(quantidade)
        else: 
            corre = input("deseja correr?: (s / n): ")
            if corre == "s":
                self.correr()
    
    def cobrir(self, aposta):
        cobre = input("deseja cobrir a aposta? (s / n): ")
        if cobre == "s":
            if self.dinheiro >= aposta:
                self.dinheiro -= aposta
            else: 
                win = input("deseja dar a win? (s / n): ")
                if win == "s":
                    self.dinheiro = 0
            self.correr()

    def correr(self):
        jogo.baralho()
        for i in range(2):
            Jogo.baralho.append(self.cartas[i])
            Jogo.rodada.remove(Jogador)
        self.cartas = []

class Jogo(object):
    def __init__(self, baralho):
        self.jogadores = self.add_jogadores()
        self.baralho = baralho
        self.mesa = []
        self.dinheiro_mesa = 0
        self.rodada = [self.jogadores[0]]
    
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
                pass
                print(error)    
        for i in range(num):
            nome = input("Nome do jogador: ")
            player = Jogador(nome)
            jogadores.append(player)
        return jogadores


    def calcular_vencedor(self):
        for i in range(9):
            player = self.jogadores[i]
            player.valor = 0
            if player.cartas == []:
                pass
            else:
                pass
    
    def rodadas(self):
        i = 0
        while i < 5 and self.rodada != []:
            self.jogadores[0].jogar()
            i += 1
            print(self.jogadores[0].cartas)
            print(self.mesa)

if __name__ == "__main__":
    start = Jogo(baralho) 
    start.dar_cartas()          
    start.rodadas()