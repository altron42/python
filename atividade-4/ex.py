# Universidade Federal do Amazonas
# Instituto de Computação
# Introducação a Computação
# Prof Alberto Castro
# Atividade 6 - Exercício 1
# Aluno: Micael S Pimentel
# Data: 08/06/2018

from math import *

def norep(xs,dup=None):
	if len(xs)<2: return xs
	if dup is not None:
		try:
			xs.remove(dup)
			norep(xs, dup)
		except ValueError:
			pass
	return [head(xs)] + norep(tail(xs), head(xs))

def norep2(xs):
	if len(xs)<2: return xs
	elif head(xs)==head(tail(xs)): xs.remove(head(xs))
	return [head(xs)] + norep(tail(xs))

def head(xs):
	return xs[0]

def tail(xs):
	return xs[1:]
