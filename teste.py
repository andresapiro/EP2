def define_posicoes(linha, coluna, orientacao, tamanho):
    lista_posicao = [[linha, coluna]]
    contador =1
    for e in range(tamanho-1):
        if orientacao == 'vertical':
            lista_posicao.append([linha+contador, coluna])
            contador +=1
        else:
            lista_posicao.append([linha, coluna+contador])
            contador +=1
    return lista_posicao