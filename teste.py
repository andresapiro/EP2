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

def preenche_frota(dicionario_frota, nome_navio, linha, coluna, orientacao, tamanho):
    lista_posicao = define_posicoes(linha, coluna, orientacao, tamanho)
    if nome_navio not in dicionario_frota:
        dicionario_frota[nome_navio] = [lista_posicao]
    else:
        dicionario_frota[nome_navio].append(lista_posicao)
    return dicionario_frota


def faz_jogada(tabuleiro, linha, coluna):
    if tabuleiro[linha][coluna] == 0:
        tabuleiro[linha][coluna] = '-'
    
    if tabuleiro[linha][coluna] == 1:
        tabuleiro[linha][coluna] = 'X'
    return tabuleiro