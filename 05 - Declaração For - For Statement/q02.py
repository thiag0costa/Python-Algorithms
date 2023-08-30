#todo Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.

for num in range(1, 51):
    print('.', end='')
    if num % 2 == 0:
        print("O número {} é par".format(num))

# Forma 2 de fazer, aqui usa metade do processador porque não faz 2 laços de cada vez. Com o passo 2 é dividido por 2 o processamento e os laços.
#for n in range(2, 51, 2):
#    print('.', end = '')
#    print(n, end = '')
#print('Acabou.')
