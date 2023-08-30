#todo Crie um programa que leia um número inteiro e mostre na tela se ele é par ou ímpar.
num = int(input('Digite um número inteiro qualquer. '))
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7;30m'}
resultado = num % 2
if resultado == 0:
    print('O número digitado {}{}{} é {}par.{}'.format(cores['azul'], num, cores['limpa'], cores['azul'], cores['limpa']))
else:
    print('O número digitado {}{}{} é {}ímpar.{}'.format(cores['amarelo'], num, cores['limpa'], cores['amarelo'], cores['limpa']))
