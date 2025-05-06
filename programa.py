import funcoes as fc
cart=[]
for t in range(1,12):
    fc.imprime_cartela(cart)
    rolados=fc.rolar_dados(5)
    guardados=[]
    uso_r=2
    print('Dados rolados: ')
    print('Dados guardados: ')
    opc=int(input("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:"))
    while opc!=0:
        if opc==1:
            g=int(input("Digite o índice do dado a ser guardado (0 a 4):"))
            gi=fc.guardar_dado(rolados,guardados,g)
            rolados=gi[0]
            guardados=gi[1]
        elif opc==2:
            r=int(input("Digite o índice do dado a ser removido (0 a 4):"))
            ri=fc.remover_dado(rolados,guardados,r)
            rolados=ri[0]
            guardados=ri[1]
        elif opc==3:
            if uso_r>0:
                rolados=fc.rolar_dados(len(rolados))
            else:
                print("Você já usou todas as rerrolagens.")
        elif opc==4:
            fc.imprime_cartela(cart)
        else:
            print("Combinação inválida. Tente novamente.")
        