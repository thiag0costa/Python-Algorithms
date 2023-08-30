#todo Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
#todo 1 - para binário ; 2 - para octal ; 3 - para hexadecimal
num = int(input('Digite um número inteiro: '))
print('Escolha uma das bases para conversão:')
print('1 - para BINÁRIO')
print('2 - para OCTAL')
print('3 - para HEXADECIMAL')
print('Selecione uma das opções acima digitando um número de 1 a 3.')
opçao = int(input('Sua opção: '))
if opçao == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(num, bin(num)[2:])) #O [2:] foi colocado para não mostrar se é bin, oct ou hex (são os 2 primeiros)
elif opçao == 2:
    print('{} convertido para OCTAL é igual a {}'.format(num, oct(num)[2:]))
elif opçao == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(num, hex(num)[2:]))
else:
    print('Digite a opção correta. Deve-se escolher um número de 1 a 3.')
