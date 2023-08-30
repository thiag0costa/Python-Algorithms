#todo Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
#todo - Se ele ainda vai se alistar ao serviço militar. - Se é a hora de se alistar - Se já passou do tempo de alistamento.
#todo Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import date
ano = int(input('Digite o ano de nascimento, com 4 números. '))
idade = date.today().year - ano
print('Quem nasceu em {} tem {} ano(s) em {}.'.format(ano, idade, date.today().year))
if idade == 18:
    print('Está na hora de você se alistar IMEDIATAMENTE.')
elif idade < 18:
    faltam = 18 - idade
    print('Ainda não está na hora de você se alistar, ainda faltam {} ano(s).'.format(faltam))
    print('Seu alistamento será em {}.'.format(date.today().year + faltam))
else:
    passados = idade - 18
    print('Você já deveria ter se alistado há {} ano(s).'.format(passados))
    print('Seu alistamento foi em {}.'.format(date.today().year - passados))
