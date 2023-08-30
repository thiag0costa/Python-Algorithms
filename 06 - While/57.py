# faça um programa que leia o SEXO de uma pessoa, mas só aceite os valores "M" ou "F". Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = str(input("Digite o seu sexo - Digite M ou F\n")).upper().strip()

while True:
    if sexo != "F" and sexo != "M":
        sexo = str(input("Dados inválidos, digite o seu sexo - [M/F]\n")).upper().strip()
        continue
    else:
        break