#Programa para ler algo pelo teclado e mostrar o seu tipo primitivo e todas as informações possíveis sobre ele.
#Program to read something typed on keyboard and to show it's primitive type e all the information about it.


variavel = input('Digite algo? ')

print('O tipo primitivo desse valor é', type(variavel))
print('O tipo primitivo desse valor é {}'.format(type(variavel)))

print('Tem espaço?', variavel.isspace())
print('Tem espaço? {}'.format(variavel.isspace()))
      
print('É um número?', variavel.isnumeric())
print('É um número? {}'.format(variavel.isnumeric()))

print('É alfabético?', variavel.isalpha())
print('É alfabético? {}'.format(variavel.isalpha()))

print('É alfanumérico?', variavel.isalnum())
print('É alfanumérico? {}'.format(variavel.isalnum()))

print('Está em maiúscula?', variavel.isupper())
print('Está em maiúscula? {}'.format(variavel.isupper()))

print('Está em minúscula?', variavel.islower())
print('Está em minúscula? {}'.format(variavel.islower()))

print('Está capitalizada?', variavel.istitle())
print('Está capitalizada? {}'.format(variavel.istitle()))
