# Universidade Federal do Amazonas
# Instituto de Computação
# Introducação a Computação
# Prof Alberto Castro
# Lista 1 - Parte 1 - Bloco 2
# Aluno: Micael S Pimentel
# Data: 11/05/2018

from math import *

# P06
def pontos(mao):
	soma=0
	for pedra in mao:
		soma=soma+pontospedra(pedra[0],pedra[1])
	return soma

def pontospedra(a,b):
	return a+b
