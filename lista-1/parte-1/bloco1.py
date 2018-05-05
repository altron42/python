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
