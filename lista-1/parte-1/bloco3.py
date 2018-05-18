# Universidade Federal do Amazonas
# Instituto de Computação
# Introducação a Computação
# Prof Alberto Castro
# Lista 1 - Parte 1 - Bloco 3
# Aluno: Micael S Pimentel
# Data: 18/05/2018

from math import *

# P17
def mesap(mesa):
	if len(mesa)==4: return True;
	else: return False

# P18
def carroca_m_p(mesa):
	for pedra in mesa:
		if carrocap(pedra): return True
	return False

# P03
def carrocap(pedra):
	if len(pedra)==1: return False
	elif pedra[0]==pedra[1]: return True
	else: return False
