# Universidade Federal do Amazonas
# Instituto de Computação
# Introducação a Computação
# Prof Alberto Castro
# Atividade 2 - Exercício 3
# Aluno: Micael S Pimentel
# Data: 13/04/2018

from math import *

def pano_amarelo(x1,y1,x2,y2):
	area_c = pi*(((y1-y2)/2)**2) # area do circulo
	lado_b = ((y1-y2)*sqrt(2))/2 # lado do quadrado amarelo
	area_b = lado_b**2			  # area do quadrado aamarelo
	return area_b-area_c
