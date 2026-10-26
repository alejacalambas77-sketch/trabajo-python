from ejemplocarro import Carro

#creando un objeto de la clase Carro
unCarro = Carro("YAC123" , "Toyota", "Montero ", "Rojo Vinotinto")

print(type(unCarro))

unCarro.girarDerecha()
unCarro.girarIzquierda()
print(f"El carro es de color: {unCarro.color.upper()}")
#modifiando el color del carro
unCarro.color = "Negro Brillante"
print(f"El carro es de color: {unCarro.color.upper()}")

otroCarro = Carro("XYZ789", "Nissam", "GT-R", "Blanco")
print(f"El otro carro es de color: {otroCarro.color.upper()}")

unCarro.acelerar(20)
unCarro.acelerar(30)

