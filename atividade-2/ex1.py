# Universidade Federal do Amazonas
# Instituto de Computação
# Introducação a Computação
# Prof Alberto Castro
# Atividade 2 - Exercício 1
# Aluno: Micael S Pimentel
# Data: 13/04/2018

from math import *

def intersec(x1,y1,x2,y2,x3,y3,x4,y4):
	if (x1>x4 or x3>x2 or y1<y4 or y3<y2):
		return False
	else:
		return True
