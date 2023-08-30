# leia o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while

primeiroTermo = int(input("Digite o primeiro termo. "))
razao = int(input("Qual é a razão da progressão aritmética? "))
cont = 1
n = 0
while cont < 11:
    termos = primeiroTermo + razao*n
    n += 1
    print(termos, end=' - ')
    cont += 1
print("Fim")

