#todo Refaça o desafio 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
#todo - Equilátero: todos os lados iguais - Isósceles: dois lados iguais - Escaleno: todos os lados diferentes
print('-=' * 15)
print('Analisando...')
print('-=' * 15)
reta1 = float(input('Digite o comprimento da primeira reta. '))
reta2 = float(input('Digite o comprimento da segunda reta. '))
reta3 = float(input('Digite o comprimento da terceira reta. '))
if (reta1 < reta2 + reta3) and (reta2 < reta1 + reta3) and (reta3 < reta1 + reta2):
    print('Os segmentos acima PODEM FORMAR um triângulo ', end='')
    if reta1 == reta2 == reta3:
        print('EQUILÁTERO.')
    elif reta1 != reta2 != reta3 != reta1:
        print('ESCALENO.')
    else:
        print('ISÓSCELES.')
else:
    print('NÃO é possível formar um triângulo.')
