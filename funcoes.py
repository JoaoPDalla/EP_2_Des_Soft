def rolar_dados(quant_dado):
    import random 
    list_dado=[]
    for i in range(0,quant_dado):
        list_dado.append(random.randint(1,6))
    return list_dado
def guardar_dado(rolados,guardados,dado):
    guardados.append(rolados[dado])
    del rolados[dado]
    return [rolados,guardados]
def remover_dado(rolados,guardados,dado):
    rolados.append(guardados[dado])
    del guardados[dado]
    return [rolados,guardados]