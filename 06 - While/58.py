# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 10 e peça para o jogador descobrir qual foi o número escolhido pelo computador. O jogador deve tentar adivinhar até acertar, mas sempre dizendo ao jogador se o número escolhido pelo computador está acima ou abaixo do número escolhido pelo jogador. Ao final, deve-se mostrar quantos palpites foram dados pelo jogador.
from random import randint

escolha = randint(1,10)
contPalpites = 0
while True:
    contPalpites += 1
    entrada = int(input("Digite um número: "))
    if entrada == escolha:
        print(f"Parabéns! Você acertou o número {escolha}, tentando {contPalpites} vez(es) para isso.")
        break
    elif entrada < escolha:
        print(f"O número digitado é menor que o escolhido pelo computador.")
    elif entrada > escolha:
        print(f"O número digitado é maior que o escolhido pelo computador.")

