#todo Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do
#todo comprador e em quantos anos ele vai pagar. Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então
#todo o empréstimo será negado.
valorcasa = float(input('Qual o preço do imóvel? R$'))
salario = float(input('Quanto você ganha por mês? R$'))
anos = int(input('Em quantos anos você quer pagar? '))
parcelamensal = (valorcasa / anos) / 12
print('Para pagar uma casa de R${:.2f} em {:.0f} anos a prestação será de R${:.2f}.'.format(valorcasa, anos, parcelamensal))
if parcelamensal <= (salario * 0.30):
    print('Empréstimo CONCEDIDO! O valor da sua prestação será de {:.2f} ao mês'.format(parcelamensal))
else:
    print('Seu empréstimo foi NEGADO, você não tem renda suficiente para financiar o valor de R${:.2f}'.format(valorcasa))
