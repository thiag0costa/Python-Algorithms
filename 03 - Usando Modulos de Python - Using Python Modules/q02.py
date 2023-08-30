#Ler o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcular e mostrar o comprimento
#da hipotenusa

# Read the length of the opposite and adjacent sides of a right triangle. Calculate and display the length of the hypotenuse.

#MODO 01
# Soluetion 01

#c1 = float(input('Qual o comprimento do cateto oposto? '))
#2 = float(input('Qual o comprimento do cateto adjacente? '))
#h = (pow(c1, 2) + pow(c2, 2)) ** (1/2)
#print('Para um cateto oposto de {} e um cateto adjacente de {} a hipotenusa é igual a {:.2f}'.format(c1, c2, h))

#MODO 02
# Solution 02
from math import hypot
c1 = float(input('Comprimento do cateto oposto: '))
c2 = float(input('Comprimento do cateto adjacente: '))
hi = hypot(c1, c2)
print('Para um cateto oposto de {} e um cateto adjacente de {} a hipotenusa é igual a {:.2f}'.format(c1, c2, hi))
