#todo Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
# - Média abaixo de 5.0: REPROVADO - Média entre 5.0 e 6.9: Recuperação - Média 7.0 ou superior: APROVADO
nota = float(input('Digite a sua primeira nota. '))
nota2 = float(input('Digite a sua segunda nota. '))
media = (nota + nota2) / 2
print('Tirando {} e {}, a média do aluno é {:.2f}.'.format(nota, nota2, media))
if media < 5:
    print('O aluno está REPROVADO.')
elif 5 <= media <= 6.9:
    print('O aluno está em RECUPERAÇÃO.')
else:
    print('O aluno está APROVADO.')
