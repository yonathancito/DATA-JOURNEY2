# bucles for (repetir instrucciones varias veces)
regiones = ['lima', 'arequipa', 'cusco']
for re in regiones:
    print(re)

# acumuladores
ventas = [100, 200, 300, 400, 500, 600]
total = 0
for ve in ventas:
    total += ve
print(f'ventas {total}')
print(f'promedio ventas {total/len(ventas)}')

# bucles while (repite mientras instruccion sea verdadera)
numero = 0
while numero < 10:
    numero += 1
    print(numero)

num = 0
while ventas[num] < 500:
    print(ventas[num])
    num += 1

# ejercicio
ventas = [100, 3000, 7000, 500]
for ve in ventas:
    if ve > 2000:
        print(f'su venta de {ve} es alta')
    else:
        print(f'su venta de {ve} es baja')
