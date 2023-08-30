#todo Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram no intervalo
#todo de 1 até 500.
soma = 0
for num in range(1, 501):
    if num % 2 == 1:
        if num % 3 == 0:
            soma += num
            print(soma)

# Forma 02
#soma = 0
#cont = 0
#for c in range(1, 501, 2):
#    if c % 3 == 0:
#        soma += c
#        cont += 1
#print('A soma de todos os {} valores solicitados é {}'.format(cont, soma))
