#Pergunta a quantidade de km rodados de um carro alugado e a quantidade de dias pelos quais ele foi alugado, retornando o preço a pagar,
#sabendo que o carro custa R$60 por dia e R$0,15 por km rodado.

# The program asks how many km the rented car has driven and for how long, in days, the car was rent, displaying the price to be paid, knowing that the 
# car costs R$60 per day e R$0,15 for each km.

dias = float(input('Por quantos dias o carro foi alugado? '))
kmrodados = float(input('Quantos km rodou o carro? '))
preçofinal = (dias * 60) + (kmrodados * 0.15)
print('O preço final a ser pago é de: R${:.2f}'.format(preçofinal))
