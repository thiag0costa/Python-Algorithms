# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados
# exemplo: digite um número: 1834 
# resposta: unidade:4 dezena:3 centena: 8 milhar: 1
# dá pra fazer usando string ou matematicamente.

# Write a program that reads a number from 0 to 9999 e display on screen each digit separated
# ex: type a number: 1834 
# answer: unidades (ones): 4 dezenas (tens): 3 centenas (hundreds): 8 milhares (thousands): 1

num = int(input('Digite um número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analisando o número {}'.format(num))
print('Unidade(s): {}'.format(u))
print('Dezena(s): {}'.format(d))
print('Centena(s): {}'.format(c))
print('Milhar(es): {}'.format(m))
