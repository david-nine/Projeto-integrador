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
    pontos.append([0, 0])
    
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
            pontos.append([i, i])
            pontos = igual(pontos, valor_mao)

#trinca
        if x == 3:
            pontos = [4]
            pontos.append([i, i])
            pontos = igual(pontos, valor_mao)         

#quadra
        if x == 4:
            pontos = [8]
            pontos.append([i, i])
            pontos = igual(pontos, valor_mao)
            return pontos

    for i in range(1, 15):
        x = valor_mao.count(i)
        if x == 2:
            for cont in range(i+1, 15):
                y = valor_mao.count(cont)
                if y == 3:
                    pontos = [7]
                    pontos.append([cont, i])
                    igual(pontos, valor_mao)
                    return pontos
                    
                if y == 2:
                    pontos = [3]
                    pontos.append([cont, i])
                    igual(pontos, valor_mao)    

        if x == 3:
            for cont in range(valor_mao[x], 15):
                y = valor_mao.count(cont)
                if y == 2 or y == 3:
                    pontos = [7]
                    mao = [valor_mao[-1], valor_mao[-2]]
                    mao = sorted(mao)
                    y = [mao[1], mao[0]]
                    if valor_mao[5] == i and valor_mao[6] == i or valor_mao[5] == x and valor_mao[6] == x or valor_mao[5] == x and valor[6] == i or valor_mao[5] == x and valor[6] == i:
                        pontos.append(y)
                        pontos.append([0, 0])
                    elif valor_mao[5] != x and valor_mao[6] != i:
                        pontos.append([0, 0])
                        pontos.append(y)                        
                    elif valor_mao[5] != i and valor_mao[6] == x:
                        pontos.append([valor_mao[6], 0])
                        pontos.append([valor_mao[5], 0])
                    elif valor_mao[5] == i and valor_mao[6] != x:
                        pontos.append([valor_mao[5], 0])
                        pontos.append([valor_mao[6], 0])
                    return pontos

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
                if mesa[-2][-1] == letras[i] and mesa[-1][-1] == letras[i]:
                    a = sorted([valor_mao[-2], valor_mao[-1]])    
                    a = [a[1], a[0]]
                    pontos.append(a)
                    pontos.append(a)
                elif mesa[-2][-1] != letras[i] and mesa[-1][-1] != letras[i]:
                    a = sorted([valor_mao[-2], valor_mao[-1]])    
                    a = [a[1], a[0]]
                    pontos.append([0, 0])
                    pontos.append(a)
                elif mesa[-2][-1] == letras[i]:
                    pontos.append([valor_mao[-2], 0])
                    pontos.append([valor_mao[-1], 0])
                elif mesa[-1][-1] == letras[i]:
                    pontos.append([valor_mao[-1], 0])
                    pontos.append([valor_mao[-2], 0])
                return pontos

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
                if valor_mao[5] in lista and valor_mao[6] in lista:
                    a = sorted([valor_mao[5],valor_mao[6]])
                    pontos.append([a[1], a[0]])
                    pontos.append([0, 0])
                elif valor_mao[5] in lista:
                    pontos.append([valor_mao[5], 0])
                    pontos.append([valor_mao[6], 0])
                elif valor_mao[6] in lista:
                    pontos.append([valor_mao[6], 0])
                    pontos.append([valor_mao[5], 0])
                else:
                    pontos.append([0, 0])
                    igual(pontos, valor_mao)
    
    pp = flush(mesa, valor_mao, 7)
    if pp:
        if pontos[0] == 5 and pp[0] == 6:    
            pontos[0] = 9
        else:
            pontos = pp 
    return pontos

valor = calcular_mao(["1p", "Kp"], ["5o","10o","2e","8p","4e"])
print(valor)