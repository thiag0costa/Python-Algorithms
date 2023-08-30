#todo Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade
#todo e quantas já são maiores. Maioridade >= 21 anos
from datetime import date
contMAIOR = 0
contMENOR = 0
for i in range(1, 8):
    var = int(input('Digite o ano de nascimento da {}ª pessoa.'.format(i)))
    anoAtual = date.today().year
    dif = anoAtual - var
    if dif >= 21:
        contMAIOR += 1
    else:
        contMENOR += 1
print(f'{contMAIOR} são maiores de idade e {contMENOR} são menores de idade.')
