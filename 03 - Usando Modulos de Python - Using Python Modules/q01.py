# Ler número real e mostre na tela sua porção inteira
# Read a real number e display on screen it's whole part.

#MODO 01
#SOLUTION 01
import math
num = float(input('Digite um número: '))
print('A porção inteira do número digitado é {}.'.format(math.trunc(num)))

#MODO 02
#SOLUTION 02
#from math import trunc
#num = float(input('Digite um número: '))
#print('A porção inteira do número digitado é {}.'.format(trunc(num)))

#MODO 03
#SOLUTION 03
#num = float(input('Digite um número: '))
#print('A porção inteira do número digitado é {}.'.format(int(num)))
