#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar. Considerar 1U$ = 3,27R$
#Create a program that reads how much money someone possess in it's wallet and print how many dollars is possible to purchase. Consider 1U$ = 3,27R$

var = float(input('Quantos reais você tem na sua carteira? R$ '))
dolar = 1/3.27
conversao = var * dolar
print('Com R$ {:.2f} você pode comprar {:.2f} dólares'.format(var, conversao))
