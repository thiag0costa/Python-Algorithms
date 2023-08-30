# Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma sequência de Fibonacci.
# Ex: 0 - 1 - 1 - 2 - 3 - 5 - 8

while True:
    lista = [0,1]
    entrada = int(input("Quantos números da sequência Fibonacci você deseja ver? Digite 0 para sair do programa."))
    if entrada < 0:
        print("Número inválido. Digite um número maior que zero.")
    elif entrada == 0:
        print("Saindo do programa...")
    elif entrada == 1:
        print(lista[0],"- FIM")
    elif entrada == 2:
        print(lista[0],"-", lista[1]," - FIM")
    else:    
        seguinte = lista[0] + lista [1]
        for i in range(2, entrada):
            lista.append(seguinte)
            seguinte = lista[i-1] + lista[i]
        #print(lista)
        for i in lista:
            print(i, end = ' - ')
        print("FIM")
        #print("\n")

 
