# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
# Write a program that reads a person's name and return if there is "SILVA" in it's name.

nome = str(input('Digite um nome: ')).strip()
print('O nome {} tem "SILVA" no nome? {}'.format(nome, 'SILVA' in nome.upper()))
