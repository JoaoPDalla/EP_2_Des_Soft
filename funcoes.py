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
#Exercicos 6 = Luís Felipe:
def calcula_pontos_sequencia_baixa(face_dado):
    for i in face_dado:
        if i+1 in face_dado and i+2 in face_dado and i+3 in face_dado:
            return 15
    return 0
#Exercicos 7 = Luís Felipe:
def calcula_pontos_sequencia_alta(face_dado):
    for i in face_dado:
        if i+1 in face_dado and i+2 in face_dado and i+3 in face_dado and i+4 in face_dado:
            return 30
    return 0
#Exercicos 8 = Luís Felipe:
def calcula_pontos_full_house(face_dado):
    numeros = []
    contagens = []
    soma=0
    for i in range(len(face_dado)):
        numero = face_dado[i]
        if numero not in numeros:
            numeros.append(numero)
            cont = 0
            for j in range(len(face_dado)):
                if face_dado[j] == numero:
                    cont += 1
            contagens.append(cont)
    if len(contagens) == 2:
        if (2 in contagens and 3 in contagens):
            for n in face_dado:
                soma+=n
            return soma
    return 0
