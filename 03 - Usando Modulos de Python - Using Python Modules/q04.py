# Sorteio de 4 alunos para apagar o quadro. Fazer um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.
# Raffle 4 students to erase the board. Write a program to help, reading their names, rafflingo them and displaying the chosen student.

from random import choice
aluno1 = str(input('Digite o nome do primeiro aluno. '))
aluno2 = str(input('Digite o nome do segundo aluno. '))
aluno3 = str(input('Digite o nome do terceiro aluno. '))
aluno4 = str(input('Digite o nome do quarto aluno. '))
lista = [aluno1, aluno2, aluno3, aluno4]
print('Dentre os alunos(as) {}, {}, {} e {} o escolhido para apagar o quadro foi {}.'.format(aluno1, aluno2, aluno3, aluno4, choice(lista)))
