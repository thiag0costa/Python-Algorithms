# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
# ex: Ana Maria de Souza
# primeiro = Ana
# último = Souza

# Write a program that reads a full name's person, displaying afterwards the first and the last name separately
# ex: Ana Maria de Souza
# first = Ana
# last = Souza

nome = str(input('Digite o seu nome completo. ')).strip()
nome1 = nome.split()
ultimo = nome1[len(nome1) - 1]
print('Para o nome {}, o primeiro nome é {} e o último sobrenome é {}.'.format(nome, nome1[0], ultimo))
