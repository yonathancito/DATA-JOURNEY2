# Condicionales if - else
edad = 19  # int(input("Cual es tu edad?"))
if edad >= 18:
    print('eres mayor de edad')
else:
    print('eres menor de edad')

# Multiples condicionales if-elif-else
ventas = 1000
if ventas >= 5000:
    print('Excelente')
elif ventas >= 2000 and ventas < 5000:
    print('Bueno')
else:
    print('Bajo')

# Operadores logicos
compra = 1500
if compra > 1000:
    print(f'Descuento es 10% = {compra*(10/100)}')
else:
    print('No tiene descuento')
