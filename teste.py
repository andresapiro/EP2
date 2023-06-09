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

def posiciona_frota(dicionario_frota):
    grid = [    
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
  ]

    for lista_grande in dicionario_frota.values():
        for lista1 in lista_grande:
            for lista2 in lista1:
                grid[lista2[0]][lista2[1]] = 1
    return grid

def afundados(dicionario_frota, grid):
    navios_afundados = 0
    for lista_grande in dicionario_frota.values():
        for lista1 in lista_grande:
            for lista2 in lista1:
                grid[lista2[0]][lista2[1]] = 1

    

    
    return navios_afundados
def afundados(dicionario_frota, grid):
    i = 0
    afundado = 0
    for posicao_barcos in dicionario_frota.values():
        for barcos in posicao_barcos:
                for cordenada in barcos:
                    if dicionario_frota["porta-aviões"] == posicao_barcos:
                        if grid[cordenada[0]][cordenada[1]] == 'X':
                            i += 1
                        if i == 4:
                            afundado += 1
                            i = 0
                    if dicionario_frota["submarino"] == posicao_barcos:
                        if grid[cordenada[0]][cordenada[1]] == 'X':
                            i += 1
                        if i == 1:
                            afundado += 1
                            i = 0
                    if dicionario_frota["navio-tanque"] == posicao_barcos:
                        if grid[cordenada[0]][cordenada[1]] == 'X':
                            i += 1
                        if i == 3:
                            afundado += 1
                            i = 0
                            
                    if dicionario_frota["contratorpedeiro"] == posicao_barcos:
                        if grid[cordenada[0]][cordenada[1]] == 'X':
                            i += 1
                        if i == 2:
                            afundado += 1
                            i = 0
                    
                i = 0
    return afundado
