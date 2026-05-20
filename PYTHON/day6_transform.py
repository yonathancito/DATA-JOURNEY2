ventas = [500, 1200, 7000, 4500, 800]


# Suma de ventas
total = sum(ventas)
print(total)

# Promedio de ventas
promedio = total/len(ventas)
print(promedio)

# Venta Maxima y venta minima
print(max(ventas))
print(min(ventas))

# Clasificar Ventas

for vent in ventas:
    if vent > 5000:
        print(f'{vent} -> alta')
    elif vent > 1000:
        print(f'{vent} -> media')
    else:
        print(f'{vent} -> baja')

# ventas altas en un nuevo arreglo
ventas_altas = []
for ve in ventas:
    if ve > 3000:
        ventas_altas.append(ve)

print(f'ventas altas son {ventas_altas}')

# Relacionar datos vendedores con ventas
vendedores = ['Ana', 'Luis', 'Maria', 'Pedro', 'Lucia', 'Carlos']
for i in range(len(ventas)):
    print(f'{vendedores[i]} , {ventas[i]}')

# Generar Patrones

for i in range(len(ventas)):
    if ventas[i] > 5000:
        print(f'{vendedores[i]} es top seller')

# Generan mas ingresos
for i in range(len(ventas)):
    if ventas[i] > 1000:
        print(f'{vendedores[i]} -> {ventas[i]}')

# Porcentaje de Ventas Altas
numero_ventas_totales = len(ventas)
numero_ventas_altas = 0
for v in ventas:
    if v > 1500:
        numero_ventas_altas += 1
porcentaje = (100*numero_ventas_altas/numero_ventas_totales)
print(f'porcentaje ventas altas -> {porcentaje}')
