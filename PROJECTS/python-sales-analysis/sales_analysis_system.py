ventas = [500, 1200, 7000, 300, 4500, 800]
vendedores = ['Ana', 'Luis', 'Maria', 'Pedro']

# total ventas
ventas_totales = 0
for ve in ventas:
    ventas_totales += ve
print(f'ventas totales {ventas_totales}')

# calcular promedio
promedio = ventas_totales/len(ventas)
print(f'promedio {promedio}')

# clasificar ventas // contar ventas altas
ventas_altas = 0
for ve in ventas:
    if ve > 5000:
        print(f'{ve} alta')
        ventas_altas += 1
    elif ve > 1000:
        print(f'{ve} media')
    else:
        print(f'{ve} baja')

print(f'hay en total {ventas_altas} ventas altas')

print("------------REPORTE VENTAS--------------")
print(f'Total: {ventas_totales}')
print(f'Promedio: {promedio}')
print(f'Ventas Altas: {ventas_altas}')
