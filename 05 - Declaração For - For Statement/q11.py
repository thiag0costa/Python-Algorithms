#todo Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
#todo A média de idade do grupo.
#todo Qual é o nome do homem mais velho.
#todo Quantas mulheres têm menos de 20 anos.
listaIdades = []
listaHomens = []
listaIdadeHomem = []
contaIdades = 0
cont = 0
for i in range(4):
    nomes = str(input('Digite o nome da pessoa.'))
    idades = int(input('Digite a idade da pessoa.'))
    sexos = str(input('Digite o sexo da pessoa - F ou M.'.lower().strip()))
    listaIdades.append(idades)
    contaIdades += listaIdades[i]
    if sexos == 'm':
        listaHomens.append(nomes)
        listaIdadeHomem.append(idades)
    if sexos == "f" and idades < 20:
        cont += 1

mediaIdade = contaIdades / 4

velho = max(listaIdadeHomem)
posVelho = listaIdadeHomem.index(velho)
buscaVelho = listaHomens[posVelho]

print(f'A idade média do grupo é de: {mediaIdade} anos.\nO nome do homem mais velho é: {buscaVelho}\n{cont} mulher(es) tem menos de 20 anos.')

# Modo 02
#somaidade = 0
#mediaidade = 0
#maioridadehomem = 0
#nomevelho = ''
#totmulher20 = 0
#for p in range(1, 5):
#    print('----- {}ª PESSOA -----'.format(p))
#    nome = str(input('Nome: ')).strip()
#    idade = int(input('Idade: '))
#    sexo = str(input('Sexo [M/F]: ')).strip()
#    somaidade += idade
#    if p == 1 and sexo in 'Mm':
#        maioridadehomem = idade
#        nomevelho = nome
#    if sexo in 'Mm' and idade > maioridadehomem:
#        maioridadehomem = idade
#        nomevelho = nome
#    if sexo in 'Ff' and idade < 20:
#        totmulher20 += 1
#mediaIdade = somaidade / 4
#print('A média de idade do grupo é de {} anos.'format(mediaIdade))
#print('O homem mais velho tem {} anos e se chama {}.'format(maioridadehomem, nomevelho))
#print('Ao todo são {} mulheres com menos de 20 anos.'format(totmulher20))
