# Universidade Federal do Amazonas
# Instituto de Computação
# Introducação a Computação
# Prof Alberto Castro
# Atividade 7 - Exercício 1
# Aluno: Micael S Pimentel
# Data: 15/06/2018

from math import *

def arruma(mao):
	return sorted(mao)

def completa_seq(mao,naipe):
	lista = [x[1] for x in mao if x[0]==naipe]
	if len(lista)<2: return []
	else:
		menor=lista[0]
		maior=lista[-1]
		return list(set(range(menor,maior+1)).difference(lista))

def maiorseq(mao):
	contagemCopas = len([x for x in mao if x[0]=='c'])
	contagemEspadas = len([x for x in mao if x[0]=='e'])
	contagemOuros = len([x for x in mao if x[0]=='o'])
	contagemPaus = len([x for x in mao if x[0]=='p'])
	return max(contagemCopas,contagemEspadas,contagemOuros,contagemPaus)
