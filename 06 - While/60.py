# Faça um programa que leia um número qualquer e mostre o seu fatorial.
# Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120

while True:
    entrada = int(input("Digite um número para saber o seu fatorial: "))
    if entrada < 0:
        print("Não existe fatorial de número negativo. Digite um número maior ou igual a zero. ")
        break
    fat = 1
    for i in range (1, entrada+1):
        fat = fat * i
    print(fat)
