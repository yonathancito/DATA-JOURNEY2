# lista ventas, mostrar TOTAL, promedio, ventas bajas y ventas altas
ventas = [100, 200, 300, 400, 500, 600]
total_ventas = 0
ventas_altas = ""
ventas_bajas = ""
for ve in ventas:
    total_ventas += ve
    if ve > 400:
        ventas_altas += str(ve)+" "
    else:
        ventas_bajas += str(ve)+" "
print(f'total ventas es: {total_ventas}')
print(f'ventas bajas fueron {ventas_bajas}')
print(f'ventas altas fueron {ventas_altas}')
