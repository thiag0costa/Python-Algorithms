# Converta uma temperatura digitada em °C para °F.
# Convert the typed temperature to °C from °F.

celsius = float(input('Digite uma temperatura em °C: '))
f = celsius * 9 / 5 + 32
print('A temperatura de {:.2f} °C é igual a {:.2f} °F'.format(celsius, f))
