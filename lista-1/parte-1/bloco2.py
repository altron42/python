# Universidade Federal do Amazonas
# Instituto de Computação
# Introducação a Computação
# Prof Alberto Castro
# Lista 1 - Parte 1 - Bloco 2
# Aluno: Micael S Pimentel
# Data: 11/05/2018

from math import *

# P06
def pontos(pedras):
	soma=0
	for pedra in pedras:
		soma=soma+pontospedra(pedra[0],pedra[1])
	return soma

def pontospedra(a,b):
	return a+b

# P07
def garagem(pedras):
	soma=pontos(pedras)
	resto=soma%5
	return soma-resto
