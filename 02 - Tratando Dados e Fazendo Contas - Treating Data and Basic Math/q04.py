#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada
#Create an algorithm that reads a number and show it's double, triple e square root

var = int(input('Digite um número: '))
dobro = var * 2
triplo = var * 3
raizquadrada = var**(1/2)
print('O dobro do número é {} \no triplo do número é {} \ne a raiz quadrada é {:.2f}'.format(dobro, triplo, raizquadrada))
print('O dobro do número é {}, o triplo do número é {} e a raiz quadrada é {:.2f}'.format(dobro, triplo, raizquadrada))
