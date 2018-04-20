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
	return (nf >= 5) and (freq >= 75)

def reprovadoNota(nf):
	return nf < 5

def reprovadoFalta(freq):
	return freq < 75

# retorna lista de tuplas com alunos aprovados
def aprovados(nfs):
	return [(n,f,s) for (n,f,s) in nfs if aprovado(f,s)]

# retorna lista de tuplas com alunos reprovados por nota
def reprovadosNota(nfs):
	return [(n,f,s) for (n,f,s) in nfs if reprovadoNota(f)]

# retorna lista de tuplas com alunos reprovados por falta
def reprovadosFalta(nfs):
	return [(n,f,s) for (n,f,s) in nfs if reprovadoFalta(s)]

def reprovadosNotaFalta(nfs):
	return [(n,f,s) for (n,f,s) in nfs if not aprovado(f,s)]

#def rfinal(nfs):
