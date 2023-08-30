# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.

numeros = []
while True:
    entrada = int(input("Digite um número inteiro para saber a sua tabuada: "))
    if entrada >= 0:
        for i in range(1, 11):
            print(f"{entrada} x {i} = {entrada * i}")
    else:
        print("Programa encerrado.")
        break