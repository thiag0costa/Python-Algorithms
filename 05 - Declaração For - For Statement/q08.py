#todo Crie um programa que leia uma frase qualquer e diga se ela é palíndromo, desconsiderando os espaços.
#todo Palíndromo: É quando a leitura de uma frase é a mesma tanto de frente pra trás como de trás pra frente.
#todo Ex: Apos a sopa, a sacada da casa, a torre da derrota, o lobo ama o bolo, anotaram a data da maratona etc.
#todo Desconsiderar acentos e espaços.

frase = str(input("Digite uma frase qualquer para saber se ela é um palíndromo.")).strip().lower()
lista = list(frase)
string = ''
for elemento in lista:
    string += elemento
print('O inverso de {} é {}.'.format(frase, string[::-1]))
string = string.replace(' ', '')
if string == string[::-1]:
    print('Logo, É palíndromo.')
else:
    print('Logo, NÃO é palíndromo.')

#Modo 02
#frase = str(input('Digite uma frase: ')).strip().upper()
#palavras = frase.split()
#junto = ''.join(palavras)
#inverso = ''
#for letra in range(len(junto) - 1, -1, -1):
#    inverso += junto[letra]
#print('O inverso de {} é {}'.format(junto, inverso))
#if inverso == junto:
#    print('Temos um palíndromo!')
#else:
#    print('A frase digitada não é um palíndromo!')

#Modo 03
#frase = str(input('Digite uma frase: ')).strip().upper()
#palavras = frase.split()
#junto = ''.join(palavras)
#inverso = junto[::-1]
#print('O inverso de {} é {}'.format(junto, inverso))
#if inverso == junto:
#    print('Temos um palíndromo!')
#else:
#    print('A frase digitada não é um palíndromo!')
