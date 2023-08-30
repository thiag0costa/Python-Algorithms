#todo Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# - à vista dinheiro/cheque: 10% de desconto
# - à vista no cartão: 5% de desconto
# - em até 2x no cartão: preço normal
# - 3x ou mais no cartão: 20% de juros
print('{:=^40}'.format(' LOJAS TMC '))
preço = float(input('Digite o preço das compras R$'))
print('FORMAS DE PAGAMENTO')
print('Digite 1 - Para pagamento à vista/dinheiro/cheque')
print('Digite 2 - À vista no cartão')
print('Digite 3 - 2x no cartão')
print('Digite 4 - 3x ou mais no cartão')
opçao = int(input('Escolha uma das opções digitando de 1 a 4\n'))
if opçao == 1:
    total = preço * 0.9
    print('Sua compra de R${:.2f} vai custar ao final R${:.2f}.'.format(preço, total))
elif opçao == 2:
    total = preço * 0.95
    print('Sua compra de R${:.2f} vai custar ao final R${:.2f}.'.format(preço, total))
elif opçao == 3:
    parcela = preço / 2
    print('Sua compra de R${:.2f} vai custar ao final R${:.2f} em 2x de {:.2f}.'.format(preço, preço, parcela))
elif opçao == 4:
    parcela = int(input('Será em quantas vezes?\n'))
    parcelax = (preço * 1.20) / parcela
    print('Sua compra de R${:.2f} vai custar ao final R${:.2f} em {}x de R${:.2f} - COM JUROS.'.format(preço, preço * 1.20, parcela, parcelax))
else:
    print('Digite uma opção correta. Deve ser um número de 1 a 4.')
