#O mesmo prof do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome
#dos 4 alunos e mostre a ordem sorteada.

# The same teacher from the previous question wants to raffle the work's presentation order of his students. Write a program that reads 4 students names and display the raffled order.

from random import shuffle
aluno1 = input('Qual o nome do primeiro aluno(a)? ')
aluno2 = input('Qual o nome do segundo aluno(a)? ')
aluno3 = input('Qual o nome do terceiro aluno(a)? ')
aluno4 = input('Qual o nome do quarto aluno(a)? ')
lista = [aluno1, aluno2, aluno3, aluno4]
shuffle(lista)
print('A ordem de apresentação será:\n{}'.format(lista))
