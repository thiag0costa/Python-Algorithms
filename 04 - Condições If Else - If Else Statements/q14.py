#todo A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# - Até 9 anos: MIRIM - Até 14 anos: INFANTIL - Até 19 anos: JUNIOR - Até 25 anos: SÊNIOR - Acima: MASTER
from datetime import date
nascimento = int(input('Qual o seu ano de nascimento? com 4 números.'))
idade = date.today().year - nascimento
if idade <= 9:
    print('Sua idade é de {} anos e você pertence à categoria MIRIM'.format(idade))
elif idade <= 14:
    print('Sua idade é de {} anos e você pertence à categoria INFANTIL'.format(idade))
elif idade <= 19:
    print('Sua idade é de {} anos e você pertence à categoria JUNIOR'.format(idade))
elif idade <= 25:
    print('Sua idade é de {} anos e você pertence à categoria SÊNIOR'.format(idade))
elif idade > 25:
    print('Sua idade é de {} anos e você pertence à categoria MASTER'.format(idade))
