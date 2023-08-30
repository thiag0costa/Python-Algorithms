# leia o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while. No entanto, o programa deve perguntar para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando ele disser que quer mostrar 0 termos

primeiroTermo = int(input("Digite o primeiro termo. "))
razao = int(input("Qual é a razão da progressão aritmética? "))
cont = 1
n = 0
termosTotais = 0
mais = 10
while mais != 0:
    termosTotais += mais
    while cont <= termosTotais:
        termos = primeiroTermo + razao*n
        n += 1
        print(termos, end=' - ')
        cont += 1
    print("PAUSA")
    mais = int(input("Quantos termos a mais você deseja que sejam mostrados? "))
print(f"A progressão foi finalizada com {termosTotais} termos mostrados.")
