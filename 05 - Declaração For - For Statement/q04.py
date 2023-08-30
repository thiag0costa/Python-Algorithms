#todo Refaça o desafio 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

var = int(input("Digite um número inteiro qualquer e descubra a sua tabuada."))
print("A tabuada de {} é igual a: ".format(var))
for c in range(1, 11):
    tabuada = '{} x {} = {}'.format(var, c, c*var)
    print(tabuada)
