# Crie um programa que leia dois valores e mostre um menu na tela:
# [1] somar
# [2] multiplicar
# [3] maior
# [4] novos números
# [5] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
while True:
    escolha = int(input("[1] somar\n[2] multiplicar\n[3] maior\n[4] novos números\n[5] sair do programa\nEscolha uma opção: "))
    if escolha == 1:
        print(f"{numero1} + {numero2} = {numero1 + numero2}")
    elif escolha == 2:
        print(f"{numero1} x {numero2} = {numero1 * numero2}")
    elif escolha == 3:
        maior = [numero1, numero2]
        print(f"Entre os números {numero1} e {numero2}, o maior é o número", max(maior))
    elif escolha == 4:
        numero1 = int(input("Digite o primeiro número: "))
        numero2 = int(input("Digite o segundo número: "))
        continue
    elif escolha == 5:
        break