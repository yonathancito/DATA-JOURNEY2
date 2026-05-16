nombre_vendedor = input('Ingrese Su nombre: ')
monto_ventas = int(input('Ingrese el monto de ventas'))
if monto_ventas > 5000:
    print(f'{nombre_vendedor} su ingreso es excelente')
elif monto_ventas > 2000 and monto_ventas <= 5000:
    print(f'{nombre_vendedor} su ingreso es bueno')
else:
    print(f'{nombre_vendedor} su ingreso es bajo')
