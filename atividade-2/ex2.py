# Universidade Federal do Amazonas
# Instituto de Computação
# Introducação a Computação
# Prof Alberto Castro
# Atividade 2 - Exercício 2
# Aluno: Micael S Pimentel
# Data: 13/04/2018

from math import *

def tarifa(m):
	if (m<=5):
		return 5
	elif (m<=10):
		return 7
	else:
		return (m-10)+7
