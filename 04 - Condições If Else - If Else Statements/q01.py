#todo Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir
# qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
from random import randint
import time
var = randint(0, 5) #faz o computador "pensar"
print('-=-' * 20)
print('Vou pensar num número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
entrada = int(input('Digite um número de 0 a 5: ')) #Jogador tenta adivinhar um número
print(entrada, var)
if entrada >= 0 and entrada <= 5:
    if entrada == var:
        print('Parabéns! Você me venceu!')
    else:
        print('Ganhei! Eu pensei no número {} e não no {}!'.format(var, entrada))
else:
    print("Você digitou um número errado. Digite um número inteiro de 0 a 5.")

