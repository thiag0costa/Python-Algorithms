#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
# Write an algorithm that reads the product's price and display it's new price with a 5% discount.

var = float(input('Qual é o preço do produto? R$ '))
novopreco = var*0.95
print('O preço do produto com desconto de 5% é de: R$ {:.2f}'.format(novopreco))
