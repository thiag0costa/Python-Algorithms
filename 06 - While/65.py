# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

numeros = []
escolha = "S"
while escolha in "sS":
    entrada = int(input("Digite um ou mais números inteiros. "))
    if entrada != 0:
        numeros.append(entrada)
    escolha = str(input("Deseja continuar? [S/N] ")).upper().strip()
    if escolha == "N":
        media = int(sum(numeros)) / int(len(numeros))
        maior = max(numeros)
        menor = min(numeros)
        print(f"A média dos números digitados é igual a {media:.2f}\nO maior número digitado foi o {maior}\nO menor número digitado foi o {menor}")
        break