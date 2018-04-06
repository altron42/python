# Universidade Federal do Amazonas
# Instituto de Computação
# Introducação a Computação
# Prof Alberto Castro
# Atividade 1 
# Aluno: Micael S Pimentel
# Data: 06/04/2018

from math import *

def pd(c):
	# math.ceil(X) retorna o menor numero inteiro maior que ou igual a X 
	consumo=ceil(c)
	if(consumo <= 2):
		return 20
	elif(consumo <= 5):
		return 20+(5*consumo)
	elif(consumo <= 10):
		return 40+(3*consumo)
	else:
		return 60+(1.5*consumo)
		
def tq(x1,y1,x2,y2):
	if(x1 < 0 and y1 > 0 and x2 > 0 and y2 < 0):
		return True
	else:
		return False
