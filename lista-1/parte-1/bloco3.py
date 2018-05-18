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
	for ponta in mesa:
		if carrocap(ponta): return True
	return False

# P03
def carrocap(ponta):
	if len(ponta)==1: return False
	elif ponta[0]==ponta[1]: return True
	else: return False

# P19
def pontos_marcados(mesa):
	soma=0
	for ponta in mesa:
		soma=soma+ponta[0]
		if len(ponta)>1: soma=soma+ponta[1]
	if soma%5==0: return soma
	else: return 0
