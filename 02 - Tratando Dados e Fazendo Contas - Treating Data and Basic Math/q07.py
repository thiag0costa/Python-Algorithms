#Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada
#Write a program that reads a given whole number and show on screen it's multiplication table.

var = int(input('Digite um número para ser mostrado a sua tabuada.'))
mostra = ' \nA tabuada de {} é igual a: '.format(var)
tabuada = '\n 0 x {} = {} \n 1 x {} = {} \n 2 x {} = {} \n 3 x {} = {} \n 4 x {} = {} \n 5 x {} = {} \n 6 x {} = {} \n 7 x {} = {} \n 8 x {} = {} \n 9 x {} = {} \n10 x {} = {}'. format(var, var*0, var, var*1, var, var*2, var, var*3, var, var*4, var, var*5, var, var*6, var, var*7, var, var*8, var, var*9, var, var*10)
tracos = '-'*12
print(tracos, mostra, tabuada)
