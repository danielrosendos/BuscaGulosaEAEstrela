# coding=utf-8
########################################################################################################################
####                                  Trabalho Inteligencia Artificial - Agentes de Busca                           ####
####                                  Aluno: Daniel Rosendo de Souza                                                ####
####                                  Professor: Ajalmar                                                            ####
####                                  Arquivo agente_Teste - Arquivo que de teste do projeto                        ####
########################################################################################################################

from agentesDeBusca import GBFS, AS
from classes import Problema, ProblemaAspirador
from worlds import vaccum_world, HWV, map_romania, HSLD


aux = HWV.keys()
aux2 = HSLD.keys()

print ("---------------Busca A* Mundo Aspirador de Po------------- \n")
for i in range(len(aux)):
    for j in range(len(aux)):
        p = ProblemaAspirador(aux[i], vaccum_world)
        print (AS(p, HWV))

print ("---------------Fim Busca A* Aspirador de Po--------------- \n")

print ("---------------Busca Gulosa Mundo Aspirador de Po------------- \n")
for i in range(len(aux)):
    for j in range(len(aux)):
        p = ProblemaAspirador(aux[i], vaccum_world)
        print (GBFS(p, HWV))
print ("---------------Fim Busca Gulosa Mundo Aspirador de Po--------- \n")

p = Problema("Arad", "Bucharest", map_romania)
print (AS(p, HSLD))
print (GBFS(p, HSLD))

p = Problema("Zerind", "Bucharest", map_romania)
print (AS(p, HSLD))
print (GBFS(p, HSLD))

p = Problema("Timisoara", "Bucharest", map_romania)
print (AS(p, HSLD))
print (GBFS(p, HSLD))

p = Problema("Zerind", "Arad", map_romania)
print (AS(p, HSLD))
print (GBFS(p, HSLD))

