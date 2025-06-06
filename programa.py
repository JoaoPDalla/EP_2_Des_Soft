import funcoes as fc
cartela_de_pontos = {
    'regra_simples':  {
        1:-1,
        2:-1,
        3:-1,
        4:-1,
        5:-1,
        6:-1
    },
    'regra_avancada' : {
        'sem_combinacao':-1,
        'quadra': -1,
        'full_house': -1,
        'sequencia_baixa': -1,
        'sequencia_alta': -1,
        'cinco_iguais': -1
    }
}
pont_a=0
pont_s=0
possb=['cinco_iguais','full_house','quadra','sem_combinacao','sequencia_alta','sequencia_baixa','1','2','3','4','5','6']
possb_indice=['0','1','2','3','4']
vrfc={}
fc.imprime_cartela(cartela_de_pontos)
for t in range(0,12):
    rolados=fc.rolar_dados(5)
    guardados=[]
    uso_r=0
    print('Dados rolados: {0}'.format(rolados))
    print('Dados guardados: {0}'.format(guardados))
    print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")
    opc=input()
    while opc!='0':
        if opc=='1':
            ver_s=False
            print("Digite o índice do dado a ser guardado (0 a 4):")
            g=input()
            while ver_s!=True:
                if g in possb_indice:
                    if int(g)<len(rolados):
                        ver_s=True
                    else:
                        print("Opção inválida. Tente novamente.")
                        g=input()
                else:
                    print("Opção inválida. Tente novamente.")
                    g=input()
            gi=fc.guardar_dado(rolados,guardados,int(g))
            rolados=gi[0]
            guardados=gi[1]
        elif opc=='2':
            ver_s=False
            print("Digite o índice do dado a ser removido (0 a 4):")
            r=input()
            while ver_s!=True:
                if r in possb_indice:
                    if int(r)<len(guardados):
                        ver_s=True
                    else:
                        print("Opção inválida. Tente novamente.")
                        r=input()
                else:
                    print("Opção inválida. Tente novamente.")
                    r=input()
            ri=fc.remover_dado(rolados,guardados,int(r))
            rolados=ri[0]
            guardados=ri[1]
        elif opc=='3':
            if uso_r<2:
                rolados=fc.rolar_dados(len(rolados))
                uso_r=uso_r+1
            else:
                print("Você já usou todas as rerrolagens.")
        elif opc=='4':
            fc.imprime_cartela(cartela_de_pontos)
        else:
            print("Opção inválida. Tente novamente.")
        if opc=='1' or opc=='2' or opc=='3' or opc=='4':
            print('Dados rolados: {0}'.format(rolados))
            print('Dados guardados: {0}'.format(guardados))
            print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")
        opc=input()
    print("Digite a combinação desejada:")
    j=input()
    for i in guardados:
        rolados.append(i)
    while j not in possb or j in vrfc:
        if j not in possb:
            print("Combinação inválida. Tente novamente.")
        else:
            print("Essa combinação já foi utilizada.")    
        j=input()
    vrfc[j]=True
    cartela_de_pontos=fc.faz_jogada(rolados,j,cartela_de_pontos)
fc.imprime_cartela(cartela_de_pontos)
for s in cartela_de_pontos['regra_simples'].values():
    pont_s=pont_s+s
for a in cartela_de_pontos['regra_avancada'].values(): 
    pont_a=pont_a+a
if pont_s>62:
    pontuacao_t=pont_s+pont_a+35
else:
    pontuacao_t=pont_s+pont_a
print("Pontuação total: {0}".format(pontuacao_t))