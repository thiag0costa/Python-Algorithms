# Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiúsculas
# o nome com todas as letras minúsculas
# Quantas letras ao todo (sem considerar espaços).
# Quantas letras tem o primeiro nome

# Create a program that read a given full name person and show:
# The name with uppercase letters
# The name with lowercase letters
# How many letters has the full name (do not consider spaces)
# How many letters the first name has 

#Solution 01

nome = str(input('Qual o seu nome completo? ')).strip()
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))

#Solution 02

#separa = nome.split()
#print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))
