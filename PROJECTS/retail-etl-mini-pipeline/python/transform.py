# Datos
ventas = [500, 1200, 7000, 300, 4500, 800]
vendedores = ["Ana", "Luis", "Maria", "Pedro", "Lucia", "Carlos"]

# Calcular KPis
total = sum(ventas)
promedio = total / len(ventas)

print("Total:", total)
print("Promedio:", promedio)

# Top Seller
for i in range(len(ventas)):

    if ventas[i] > 3000:
        print(vendedores[i], "=> Top Seller")

# Ventas Premium
ventas_premium = []

for venta in ventas:

    if venta > 3000:
        ventas_premium.append(venta)

print(ventas_premium)
