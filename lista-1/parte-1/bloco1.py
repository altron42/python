# Universidade Federal do Amazonas
# Instituto de Computação
# Introducação a Computação
# Prof Alberto Castro
# Lista 1 - Parte 1 - Bloco 1
# Aluno: Micael S Pimentel
# Data: 05/05/2018

from math import *

# P01
def pedrap(a,b):
	if inteirop(a) and inteirop(b) and valorp(a) and valorp(b): return True
	else: return False

def inteirop(a):
	return isinstance(a,int)

def valorp(a):
	return not ((a < 0) or (a >6))

# P02
def maop(mao):
	if len(mao)>7: return False
	for pedra in mao:
		if not pedrap(pedra[0],pedra[1]): return False
	return True

# P03
def carrocap(a,b):
	if pedrap(a,b) and a==b: return True
	else: return False
