#todo Desenvolva um programa que leia o primeiro termo e a razão de uma P.A. No final, mostre os 10 primeiros termos dessa progressão.
primeiroTermo = int(input("Digite o primeiro termo."))
razao = int(input("Qual é a razão da progressão aritmética?"))
n = 0
for c in range(10):
    termos = primeiroTermo + razao*n
    n += 1
    print(termos)


# Modo 02
#primeiro = int(input('Primeiro termo: '))
#razao = int(input('Razão: '))
#decimo = primeiro + (10 - 1) * razao
#for c in range(primeiro, decimo + razao, razao):
#    print('{} '.format(c), end = '-> ')
#print('ACABOU')
