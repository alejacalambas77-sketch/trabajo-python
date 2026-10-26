# 1. Solicitamos los datos al usuario
nombre = input("Ingrese su nombre: ").strip()
sexo = input("Ingrese su sexo (M para mujer, H para hombre): ").strip().upper()

# 2. Convertimos la primera letra del nombre a mayúscula para comparar fácilmente
primera_letra = nombre[0].upper()

# 3. Evaluamos la lógica para asignar el grupo
if (sexo == "M" and primera_letra < "M") or (sexo == "H" and primera_letra > "N"):
    grupo = "A"
else:
    grupo = "B"

# 4. Mostramos el resultado
print(f"\nHola, {nombre.capitalize()}. Te corresponde el **Grupo {grupo}**.")