#todo Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e menor peso lidos.
maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input('Qual o peso da {}ª pessoa: '.format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso lido foi de {}Kg.'.format(maior))
print('O menor peso lido foi de {}Kg.'.format(menor))

#Modo 02
#lista = []
#for i in range(1, 6):
#    var = float(input('Digite o peso da {}ª pessoa.'.format(i)))
#    lista.append(var)
#maximo = max(lista)
#minimo = min(lista)
#print(f'O maior peso é: {maximo}Kg\nO menor peso é: {minimo}Kg')
