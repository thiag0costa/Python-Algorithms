# Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. OBS: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1 

saque = int(input("Digite quanto você quer sacar: "))

notas50 = 0
notas20 = 0
notas10 = 0
notas1 = 0
restante = 0

if saque / 50 >= 1:
    notas50 = saque // 50
    restante = saque - (notas50 * 50)
    if restante / 20 >= 1:
        notas20 = restante // 20
        restante = restante - (notas20 * 20)

if restante / 10 >= 1:
            notas10 = restante // 10
            restante = restante - (notas10 * 10)
            if restante / 1 >= 1:
                notas1 = restante // 1
                restante = restante - (notas1 * 1)

if restante / 1 >= 1:
                notas1 = restante // 1
                restante = restante - (notas1 * 1)

if saque < 50:
        notas20 = saque // 20
        restante = saque - (notas20 * 20)
        if restante / 10 >= 1:
            notas10 = restante // 10
            restante = restante - (notas10 * 10)
        if restante / 1 >= 1:
            notas1 = restante // 1
            restante = restante - (notas1 * 1)

print(f'Notas de 50: {notas50}\nNotas de 20: {notas20}\nNotas de 10: {notas10}\nNotas de 1: {notas1}\n')