#Exercicos 1 = João Pedro:
def rolar_dados(quant_dado):
    import random 
    list_dado=[]
    for i in range(0,quant_dado):
        list_dado.append(random.randint(1,6))
    return list_dado
#Exercicos 2 = João Pedro:
def guardar_dado(rolados,guardados,dado):
    guardados.append(rolados[dado])
    del rolados[dado]
    return [rolados,guardados]
#Exercicos 3 = João Pedro:
def remover_dado(rolados,guardados,dado):
    rolados.append(guardados[dado])
    del guardados[dado]
    return [rolados,guardados]
#Exercicos 4 = Luís Felipe:
def calcula_pontos_regra_simples(valor_dado):
    calculo={}
    for chave in range(1,7):
        calculo[chave]=0
    for valor in valor_dado:
        calculo[valor]=calculo[valor]+valor
    return calculo
#Exercicos 5 = Luís Felipe:
def calcula_pontos_soma(face_dado):
    soma=0
    for i in face_dado:
        soma+=i
    return soma