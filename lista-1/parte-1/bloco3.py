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

# P20
def pode_jogar_p(pedra,mesa):
	pontaA=pedra[0]
	pontaB=pedra[1]
	for ponta in mesa:
		if ponta[0]==pontaA or ponta[0]==pontaB: return True
	return False

# P21
def marca_ponto_p(pedra,mesa):
	pontaA=pedra[0]
	pontaB=pedra[1]
	temp=pontos_marcados(mesa)
	if not pode_jogar_p(pedra,mesa): return False
	for ponta in mesa:
		if carrocap(ponta):
			temp=temp-(2*ponta[0])
			if ponta[0]==pontaA:
				temp=temp+pontaB
				if carrocap(pedra): temp=temp+pontaB
				if temp%5==0:
					return True
				else:
					temp=temp-pontaB
					if carrocap(pedra): temp=temp-pontaB
			elif ponta[0]==pontaB:
				temp=temp+pontaA
				if carrocap(pedra): temp=temp+pontaA
				if temp%5==0:
					return True
				else:
					temp=temp-pontaA
					if carrocap(pedra): temp=temp-pontaA
			temp=temp+(2*ponta[0])
		else:
			temp=temp-ponta[0]
			if ponta[0]==pontaA:
				temp=temp+pontaB
				if carrocap(pedra): temp=temp+pontaB
				if temp%5==0:
					return True
				else:
					temp=temp-pontaB
					if carrocap(pedra): temp=temp-pontaB
			elif ponta[0]==pontaB:
				temp=temp+pontaA
				if carrocap(pedra): temp=temp+pontaA
				if temp%5==0:
					return True
				else:
					temp=temp-pontaA
					if carrocap(pedra): temp=temp-pontaA
			temp=temp+ponta[0]
	return False

	

















