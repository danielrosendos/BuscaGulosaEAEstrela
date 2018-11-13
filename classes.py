# coding=utf-8

########################################################################################################################
####                                  Trabalho Inteligencia Artificial - Agentes de Busca                           ####
####                                  Aluno: Daniel Rosendo de Souza                                                ####
####                                  Professor: Ajalmar                                                            ####
####                                  Arquivo Classes - Arquivo que contém as classes do projeto                    ####
########################################################################################################################

class Problema(object):

    def __init__(self, inicio, objetivo=None, acao=None):
        self.inicio = inicio
        self.objetivo = objetivo
        self.acao = acao

    def teste_de_obj(self, noEstado):
        if self.objetivo != "Bucharest":
            print ("Objetivo Não é Bucharest - Heuristica Somente Linha Reta Bucharest")
            return exit(-1)
        else:
            return noEstado == self.objetivo

    def acoes(self, noEstado):
        return list(self.acao[noEstado])

class ProblemaAspirador(object):

    def __init__(self, inicio, acao=None):
        self.inicio = inicio
        self.acao = acao

    def teste_de_obj(self, noEstado):
        if noEstado == "ELL" or noEstado == "DLL":
            return noEstado

    def acoes(self, noEstado):
        return list(self.acao[noEstado])

class No(object):

    def __init__(self, estado, pai=None, custo_caminho=0, valor=None):
        self.estado = estado
        self.pai = pai

        if pai:
            self.action = pai.estado + " -> " + estado

        self.custo_caminho = custo_caminho
        self.valor = valor
        self.profundidade = 0

        if pai:
            self.profundidade = pai.profundidade + 1

    def __repr__(self):
        return self.estado + ", " + self.action

