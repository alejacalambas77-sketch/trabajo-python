

# 1. Pedimos un número entero al usuario
numero = int(input("Ingrese un número entero: "))

# 2. Convertimos el número a binario usando la función bin() de Python
# Omitimos los dos primeros caracteres ('0b') usando [2:]
binario = bin(numero)[2:]

# 3. Mostramos el resultado por pantalla
print(f"\nEl número {numero} en notación binaria es: {binario}")