#todo Crie um programa que faça o computador jogar Jokenpô (pedra, papel e tesoura) com você.
from random import randint
from time import sleep
print('O jogo irá começar...')
print('Escolha uma das opções abaixo: ')
print('[1] - Pedra')
print('[2] - Papel')
print('[3] - Tesoura')
escolha = int(input('Digite de 1 a 3 para escolher uma das opções acima.'))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!')
sleep(1)
itens = ('zero', 'Pedra', 'Papel', 'Tesoura')
computador = randint(1, 3)
print('-=' * 11)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[escolha]))
if escolha == 1:
    if computador == 3:
        print('Você ganhou!')
    elif computador == 2:
        print('Você perdeu!')
    elif computador == 1:
        print('Empatou')
elif escolha == 2:
    if computador == 1:
        print('Você ganhou!')
    elif computador == 3:
        print('Você perdeu!')
    elif computador == 2:
        print('Empatou')
elif escolha == 3:
    if computador == 1:
        print('Você perdeu!')
    elif computador == 2:
        print('Você ganhou!')
    elif computador == 3:
        print('Empatou.')
else:
    print('Opção inválida! Digite um número inteiro de 1 a 3.')
