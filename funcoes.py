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
#Exercicos 9 = Luís Felipe:
def calcula_pontos_quadra(face_dado):
    soma=0
    for i in range(len(face_dado)):
        valor = face_dado[i]
        cont = 0
        for j in range(len(face_dado)):
            if face_dado[j] == valor:
                cont += 1
        if cont >= 4:
            for n in face_dado:
                soma+=n
            return soma
    return 0
#Exercício 10 = João Pedro Dalla
def calcula_pontos_quina(dados):
    cont={}
    for i in dados:
        if i not in cont:
            cont[i]=0
        cont[i]=cont[i]+1
        if cont[i]==5:
            return 50
    return 0
#Exercício 11 = João Pedro Dalla
def calcula_pontos_regra_avancada(dados):
    pontuc={}
    pontuc['cinco_iguais']=calcula_pontos_quina(dados)
    pontuc['full_house']=calcula_pontos_full_house(dados)
    pontuc['quadra']=calcula_pontos_quadra(dados)
    pontuc['sem_combinacao']=calcula_pontos_soma(dados)
    pontuc['sequencia_alta']=calcula_pontos_sequencia_alta(dados)
    pontuc['sequencia_baixa']=calcula_pontos_sequencia_baixa(dados)
    return pontuc
#exercício 12 = João Pedro Dalla
def faz_jogada(dados,categoria,cartela):
    car=0
    possb=['cinco_iguais','full_house','quadra','sem_combinacao','sequencia_alta','sequencia_baixa']
    if categoria in possb:
        tab=calcula_pontos_regra_avancada(dados)
        cartela['regra_avancada'][categoria]=tab[categoria]
    else:
        categoria=int(categoria)
        tab=calcula_pontos_regra_simples(dados)
        cartela['regra_simples'][categoria]=tab[categoria] 
    return cartela
def imprime_cartela(cartela):
    print("Cartela de Pontos:")
    print("-"*25)    
    for i in range(1, 7):
        filler = " " * (15 - len(str(i)))
        if cartela['regra_simples'][i] != -1:
            print(f"| {i}: {filler}| {cartela['regra_simples'][i]:02} |")
        else:
            print(f"| {i}: {filler}|    |")
    for i in cartela['regra_avancada'].keys():
        filler = " " * (15 - len(str(i)))
        if cartela['regra_avancada'][i] != -1:
            print(f"| {i}: {filler}| {cartela['regra_avancada'][i]:02} |")
        else:
            print(f"| {i}: {filler}|    |")
    print("-"*25)