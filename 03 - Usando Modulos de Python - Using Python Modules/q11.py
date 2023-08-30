# Faça um programa que leia uma frase pelo teclado e mostre: 
# 1) quantas vezes aparece a letra "A" 
# 2) em que posição ela aparece a primeira vez 
# 3) em que posição ela aparece a última vez

# Write a program that reads a phrase typed on keyboard e show: 
# 1) How many times shows the letter "A"
# 2) Wich position the letter "A" appears for the first time
# 3) Wich position the letter "A" appears for the last time.

frase = str(input('Digite uma frase. ')).strip().upper().strip()
print('A letra "a" aparece {} vezes'.format(frase.count('A')))
print('A letra "a" aparece primeiramente na posição {}.'.format(frase.find('A')+1))
print('A última vez que a letra "a" aparece é na posição {}'.format(frase.rfind('A')+1))
