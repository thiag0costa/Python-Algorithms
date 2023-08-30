# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
# a) quantas pessoas tem mais de 18 anos
# b) quantos homens foram cadastrados
# c) quantas mulheres tem menos de 20 anos

idades = []
generos = []
contMulheres = 0
contIdade = 0
contHomens = 0
while True:
    idade = int(input("----------\nCADASTRO\n----------\nIdade: "))
    idades.append(idade)
    sexo = str(input("Sexo - [M/F]: ")).lower()
    generos.append(sexo)
    if idade < 20 and sexo == "f":
        contMulheres += 1
    if idade > 18:
        contIdade += 1
    if sexo == "m":
        contHomens += 1    
    escolha = str(input("Deseja continuar cadastrando mais pessoas? [S/N]")).lower()
    if escolha != 's':
        print(f"Há {contIdade} pessoa(s) acima de 18 anos.\n{contHomens} cadastrado(s) foram homen(s).\n{contMulheres} mulher(es) tem menos de 20 anos.")
        break


