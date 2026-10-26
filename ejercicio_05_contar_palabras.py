# 1. Pedimos al usuario cuántas palabras desea ingresar
cantidad = int(input("¿Cuántas palabras deseas agregar a la lista?: "))

palabras = []

# 2. Llenamos la lista con las palabras ingresadas por el usuario
for i in range(cantidad):
    palabra_ingresada = input(f"Ingrese la palabra #{i + 1}: ").strip().lower()
    palabras.append(palabra_ingresada)

# 3. Pedimos la palabra a buscar
busqueda = input("\nIngrese la palabra que deseas buscar en la lista: ").strip().lower()

# 4. Contamos cuántas veces aparece usando el método .count()
repeticiones = palabras.count(busqueda)

# 5. Mostramos el resultado
print(f"\nLista de palabras creada: {palabras}")
print(f"La palabra '{busqueda}' aparece {repeticiones} vez/veces en la lista.")