# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".

# Create a program that reads a city's name and returns if it starts with name "SANTO".

nome = str(input('Digita o nome de uma cidade. ')).strip()
print(nome[:5].upper() == 'SANTO')
