#todo Faça um programa que leia um número inteiro e diga se ele é ou não é um número primo.

num = int(input('Digite um número: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[31m', end = '')
        tot += 1
    else:
        print('\033[m', end='')
    print('{} '.format(c), end = '')
print('\n\033[mO número {} foi divisível {} vezes.'.format(num, tot))
if tot == 2:
    print('Logo, ele é primo.')
else:
    print('Logo, ele NÃO é primo.')

# Aqui os divisores inteiros ficam em vermelho, destacados.
#num = int(input('Digite um número: '))
#for c in range(1, num + 1):
#    if num % c == 0:
#        print('\033[31m', end = '')
#    else:
#        print('\033[m', end='')
#    print('{} '.format(c), end = '')
