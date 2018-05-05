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

# P08
def pedra_igual_p(pedraA,pedraB):
	(a,b)=pedraA
	(c,d)=pedraB
	if (a==d and b==c) or (a==c and b==d): return True
	else: return False

# P09
def ocorre_pedra_p(pedra,mao):
	for pedraX in mao:
		if pedra_igual_p(pedra,pedraX): return True
	return False

# P10
def ocorre_valor_p(ponta,mao):
	if ponta<0 or ponta >6: return False
	else:
		for pedra in mao:
			if ponta==pedra[0] or ponta==pedra[1]: return True
	return False

# P11
def ocorre_pedra(ponta,mao):
	return [pedra for pedra in mao if ocorre_ponta_pedra(ponta,pedra)]

def ocorre_ponta_pedra(ponta,pedra):
	if ponta==pedra[0] or ponta==pedra[1]: return True
	else: return False
