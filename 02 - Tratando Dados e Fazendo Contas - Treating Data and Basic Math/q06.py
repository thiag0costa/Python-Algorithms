#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros
#Write a programa that reads a value in meters and show it converted in centimeters and millimeters

var = int(input('Digite um valor em metros: '))
mm = var*1000
cm = var*100
dm = var*10
dam = var*0.1
hm = var*0.01
km = var*0.001
print('Equivale a {} mm \nEquivale a {} cm \nEquivale a {} dm \nEquivale a {} dam \nEquivale a {} hm \nEquivale a {} km.'.format(mm, cm, dm, dam, hm, km))
