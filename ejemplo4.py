#listas

listaVacia = []
print(type(listaVacia))

print(listaVacia)
listaVacia.append("dato")
print(listaVacia)

paises = ["Colombia", "Peru", "Ecuador", "Brasil" , "Venezuela", "Bolivia"]

print(paises)
print ( "Longitud de la lista es" + str(len(paises)))
print(f"Longitud de la lista: {len(paises)}")

print(paises[2:4])

paises[1] = "Argentina"

print(paises)

paises.insert(2, "Chile")
print(paises)