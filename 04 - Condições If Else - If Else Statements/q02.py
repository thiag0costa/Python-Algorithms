#todo Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, moestre uma mensagem dizendo que ele foi multado.
#todo A multa vai custar R$7,00 por cada Km acima do limite.
vel = float(input('Qual a velocidade do carro? '))
if vel > 80:
    multa = (vel - 80) * 7
    print('Você foi multado. A velocidade máxima é 80Km/h! Sua multa custará R${:.2f}.'.format(multa))
else:
    print('Você não foi multado.')
