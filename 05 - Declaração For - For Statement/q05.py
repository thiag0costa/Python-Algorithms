#todo Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for
#todo ímpar, desconsidere-o.
soma = 0
for c in range(6):
    entrada = int(input("Digite um número inteiro."))
    if entrada % 2 == 0:
        soma += entrada
        print(soma)


#forma 2
#soma = 0
#cont = 0
#for c in range(1, 7):
#   num = int(input('Digite o {} valor: '.format(c)))
#    if num % 2 == 0:
#        soma += num
#        cont += 1
#print('Você informou {} números PARES e a soma foi {}'.format(cont, soma))
