# coding=utf-8

########################################################################################################################
####                                  Trabalho Inteligencia Artificial - Agentes de Busca                           ####
####                                  Aluno: Daniel Rosendo de Souza                                                ####
####                                  Professor: Ajalmar                                                            ####
####                                  Arquivo agentesDeBusca - Arquivo que contém as funções de Busca               ####
########################################################################################################################

# coding=utf-8
from classes import No
from Queue import PriorityQueue

# SOLUÇÃO
def solucao(no):
    lista = []
    custo = "Custo do Caminho: " + str(no.custo_caminho)
    while no:
        lista.append(no.estado)
        no = no.pai
    lista.reverse()
    return lista, custo

#GREEDY BEST-FIRST SEARCH - BUSCA GULOSA PELA MELHOR ESCOLHA
def GBFS(problema, heuristica):
    no = No(problema.inicio)
    fronteira = PriorityQueue()
    fronteira.put((heuristica[no.estado], no))
    explorado = set()

    while fronteira:
        aux = fronteira.get()
        no = aux[1]
        if problema.teste_de_obj(no.estado):
            return solucao(no)
        explorado.add(no.estado)

        for acao in problema.acoes(no.estado):
            custo_caminho = int(problema.acao[no.estado][acao]) + no.custo_caminho
            filho = No(acao, no, custo_caminho=custo_caminho)

            it = [i for i in fronteira.queue]
            if(heuristica[filho.estado], filho) not in it and filho.estado not in explorado:
                fronteira.put((heuristica[filho.estado], filho))


    return None

#A-ESTRELA
def AS(problema, heuristica):
    no = No(problema.inicio)
    fronteira = PriorityQueue()
    fronteira.put((heuristica[no.estado], no))
    explorado = set()

    while fronteira:
        aux = fronteira.get()
        no = aux[1]

        if problema.teste_de_obj(no.estado):
            return solucao(no)

        explorado.add(no.estado)

        for acao in problema.acoes(no.estado):
            custo_caminho = int(problema.acao[no.estado][acao]) + no.custo_caminho
            filho = No(acao, no, custo_caminho=custo_caminho)

            f_n = heuristica[filho.estado] + filho.custo_caminho
            it = [i for i in fronteira.queue]
            if (f_n, filho) not in it and filho.estado not in explorado:
                fronteira.put((f_n, filho))

    return None