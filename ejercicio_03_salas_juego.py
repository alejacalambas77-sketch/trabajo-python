# 1. Pedimos la edad al usuario
edad = int(input("Ingrese la edad del cliente: "))

# 2. Determinamos el precio según el rango de edad
if edad < 5:
    precio = 0
elif 5 <= edad <= 18:
    precio = 5000
else:
    precio = 10000

# 3. Mostramos la información por pantalla
if precio == 0:
    print("\n¡El cliente es menor de 5 años! Entrada GRATIS.")
else:
    print(f"\nEl precio de la entrada para {edad} años es de: ${precio:,} COP.")