# Ler um ângulo qualquer e mostrar na tela o valor do seno, cosseno e tangente.
# Read a given angle and display on screen the values of sine, cosine and tangent.

import math
angulo = float(input('Digite um ângulo qualquer '))
print('Para o ângulo de {}:\n Seno = {:.2f}\n Cosseno = {:.2f}\n Tangente = {:.2f}'.format(angulo, math.sin((math.radians(angulo))), math.cos((math.radians(angulo))), math.tan((math.radians(angulo)))))
