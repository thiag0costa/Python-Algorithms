# Faça um programa que leia a largura e a altura de uma parede em metros. Calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo
# que cada litro de tinta pinta uma área de 2m².

# Write a program that reads width and height of a wall in meters. Calculate it's area and the necessary amount of ink need to paint it, knowing that 
# each liter of ink paints an area of 2m².

largura = float(input('Qual a largura da parede em metros?\n'))
altura = float(input('Qual a altura da parede em metros?\n'))
area = largura * altura
qtd = area/2

print('A área da parede é de {:.2f} m² e é necessário {:.2f} litros de tinta para pintá-la.'.format(area, qtd))
