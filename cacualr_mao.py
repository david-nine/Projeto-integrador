def calcular_mao(mao, mesa):
    valor_cartas = {"1p":14,"1c":14,"1e":14,"1o":14,"2p":2,"2c":2,"2e":2,"2o":2,"3p":3,"3c":3,"3e":3,"3o":3,"4p":4,"4c":4,"4e":4,"4o":4,"5p":5,
                    "5c":5,"5e":5,"5o":5,"6p":6,"6c":6,"6e":6,"6o":6,"7p":7,"7c":7,"7e":7,"7o":7,"8p":8,"8c":8,"8e":8,"8o":8,"9p":9,"9c":9,
                    "9e":9,"9o":9,"10p":10,"10c":10,"10e":10,"10o":10,"Jp":11,"Jc":11,"Je":11,"Jo":11,"Qp":12,"Qc":12,"Qe":12,"Qo":12,"Kp":13,"Kc":13,"Ke":13,"Ko":13}
    for i in range(2):
        mesa.append(mao[i])
    valor_mao = []
    for i in range(7):
        valor_mao.append(valor_cartas[mesa[i]])

#carta alta
    pontos = [1]
    x = [valor_mao[5], valor_mao[6]]
    if x[1] >= x[0]:
        x = [x[1], x[0]]
    pontos.append(x)
    
    def igual(pontos, valor_mao):
        mao = [valor_mao[-1], valor_mao[-2]]
        mao = sorted(mao)
        y = [mao[1], mao[0]]
        pontos.append(y)
        return pontos

#dupla
    for i in range(2, 15):
        x = valor_mao.count(i)
        if x == 2:
            pontos = [2]
            pontos = igual(pontos, valor_mao)

#trinca
        if x == 3:
            pontos = [4]
            pontos = igual(pontos, valor_mao)         

#quadra
        if x == 4:
            pontos = [8]
            pontos = igual(pontos, valor_mao)
            return pontos

    for i in range(1, 15):
        x = valor_mao.count(i)
        if x == 2:
            for cont in range(i+1, 15):
                y = valor_mao.count(cont)
                if y == 3:
                    pontos = [7]
                    igual(pontos, valor_mao)
                    return pontos
                if y == 2:
                    pontos = [3]
                    igual(pontos, valor_mao)    

        if x == 3:
            for cont in range(i+1, 15):
                y = valor_mao.count(cont)
                if y == 2 or y == 3:
                    pontos = [7]
                    return igual(pontos, valor_mao)

#flush
    def flush(mesa, valor_mao, valor):
        letras = ["p", "c", "e", "o"]
        x = []
        for i in range(valor):
            x.append(mesa[i][-1])
        for i in range(4):
            y = x.count(letras[i])
            if y >= 5:
                pontos = [6]
                if 1 in valor_mao:
                    valor_mao.remove(1)
                pontos = igual(pontos, valor_mao)
#sequencia
    x = valor_mao.count(14)
    valor_novo = valor_mao
    for i in range(x):
        valor_novo.append(1)
    valor_novo = sorted(valor_novo)
    for i in range(1, 15):
        s = valor_novo.count(i)
        if s == 2:
            r = valor_novo.index(i)
            del(valor_novo[r])
        elif s == 3:
            r = valor_novo.index(i)
            del(valor_novo[r])
    for cont in range(3):
        for i in range(1,15):
            lista = [i,i+1,i+2,i+3,i+4]
            if valor_novo[cont:cont+5] == lista:
                lista_certa = lista
                pontos = [5]
                if i == 1:
                    valor_mao.remove(14)
                    valor_mao.append(1)
                igual(pontos, valor_mao)    
    pp = flush(mesa, valor_mao, 7)
    if pp:
        if pontos[0] == 5 and pp[0] == 6:    
            pontos = [9]
            igual(pontos, valor_mao)
        else:
            pontos = pp 
    return pontos

if __name__ == "__main__":
    valor = calcular_mao(["4p", "3p"], ["1p","5p","2p","5e","6c"])
    print(valor)