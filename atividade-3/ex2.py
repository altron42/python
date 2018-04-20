# Universidade Federal do Amazonas
# Instituto de Computação
# Introducação a Computação
# Prof Alberto Castro
# Atividade 3 - Exercício 2
# Aluno: Micael S Pimentel
# Data: 20/04/2018

from math import *

# dados nota final e frequencia, verifica se aprovado
def aprovado(nf,freq):
	if (nf >= 5) and (freq >= 75):
		return True
	else:
		return False

# retorna lista de tuplas com alunos aprovados
def aprovados(nfs):
	return [(n,f,s) for (n,f,s) in nfs if aprovado(f,s)]



def rfinal(nfs):
	
