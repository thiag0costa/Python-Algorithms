# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag)

lista = []
while True:
    numero = int(input("Digite um número: "))
    if numero == 999:
        break
    lista.append(numero)
soma = 0
for i in range(len(lista)):
    soma = soma + lista[i]
print(f"A soma de todos os números digitados é igual a {soma} e foram digitados {len(lista)} números.")