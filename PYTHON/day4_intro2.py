# Tipos de datos, controlan el flujo
# type()
nombre = "Ana"
print(type(nombre))
print(type(25))
print(type(19.5))
print(type(True))
# Operaciones Matematicas
# Suma, Resta, Multiplicacion, Division (respuesta), Potencia, Modulo (Residuo)
print(10+5)
print(10-5)
print(10*5)
print(10/5)
print(10**5)
print(10 % 5)
# Operaciones con Strings
nombre = 'Yonathan'
print(nombre+'Hola')
print("Data"*3)
print(nombre.upper())
print(nombre.lower())
print(len(nombre))
# Ejercicio
nombre2 = 'juan'  # input('¿Cual es tu nombre: ?')
print(nombre2.upper())
print(nombre2.lower())
print(len(nombre2))

# Listas (Coleccion organizada)

productos = ['laptop', 'mouse', 'teclado']

print(productos[0])

productos.append('Monitor')
print(len(productos))

# Ejercicios
regiones = ['Lima', 'Arequipa', 'Cusco']
print(f'la primera region es {regiones[0]}')
print(f'la ultima region es {regiones[len(regiones)-1]}')
