# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
import random

contVitoriasJogador = 0

while True:
    parOuImparComputador = random.randint(0, 1)
    numeroComputador = random.randint(0, 10)

    parOuImparJogador = str(input("Digite par ou ímpar para jogar com o computador: ")).lower()
    numeroJogador = int(input("Digite um número de 0 a 10: "))


    if parOuImparComputador == 0 and parOuImparJogador == "par" and (numeroJogador + numeroComputador) % 2 == 0:
        print("A partida terminou empatada")

    elif parOuImparComputador == 1 and parOuImparJogador == "ímpar" and (numeroJogador + numeroComputador) % 2 == 1:
        print("A partida terminou empatada")

    elif (numeroJogador + numeroComputador) % 2 == 0 and parOuImparJogador == "par" and parOuImparComputador == 1:
        print("O humano venceu a partida!")
        contVitoriasJogador += 1

    elif (numeroJogador + numeroComputador) % 2 == 1 and parOuImparJogador == "ímpar" and parOuImparComputador == 0:
        print("O humano venceu a partida!")
        contVitoriasJogador += 1

    else:
        print(f'O jogador humano venceu {contVitoriasJogador} vez(es) antes de perder a primeira partida.')
        break

