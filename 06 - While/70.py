# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar. No final, mostre:
# a) Qual é o total gasto na compra
# b) Quantos produtos custam mais de R$ 1000,00
# c) Qual é o nome do produto mais barato
produtos = []
precosProdutos = []
contAcima1000Reais = 0
omaisbarato = ""
while True:
    nomeProduto = str(input("Qual o nome do produto? ")).lower()
    produtos.append(nomeProduto)
    precoProduto = int(input("Qual o preço do produto? "))
    precosProdutos.append(precoProduto)

    gastoTotal = sum(precosProdutos)
    
    if precoProduto > 1000:
        contAcima1000Reais += 1
    
    for maisbarato in precosProdutos:
        omaisbarato = min(precosProdutos)
        for i in range(len(precosProdutos)):
            if precosProdutos[i] == omaisbarato:    
                nomeProduto = produtos[i]

    escolha = str(input("Deseja continuar? [S/N]")).lower()
    if escolha != 's':
        print(f"O total da compra foi de R${gastoTotal:.2f}\n{contAcima1000Reais} produto(s) custa(m) acima de R$1.000,00\n{nomeProduto} é o nome do produto mais barato, custando R${omaisbarato}.")
        break
