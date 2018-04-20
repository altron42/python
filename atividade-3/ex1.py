# Universidade Federal do Amazonas
# Instituto de Computação
# Introducação a Computação
# Prof Alberto Castro
# Atividade 3 - Exercício 1
# Aluno: Micael S Pimentel
# Data: 20/04/2018

from math import *

# Lista com os k primeiros elementos de uma lista xs
def take(k,xs):
	return xs[:k]
# Lista com os elementos de xs seguintes aos k primeiros
def drop(k,xs):
	return xs[k:]
# Primeiro elemento de uma lista xs
def head(xs):
	return xs[0]
# Sublista similar a xs mas sem o primeiro elemento
def tail(xs):
	return xs[1:]
# Ultimo elemento de uma lista xs
def last(xs):
	return xs[-1]
# Sublista similar a xs mas sem o ultimo elemento
def init(xs):
	return xs[:-1]
