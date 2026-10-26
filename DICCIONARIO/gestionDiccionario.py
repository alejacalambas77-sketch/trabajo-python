from diccionario import Diccionario
from palabra import Palabra

miDiccionario = Diccionario()
miDiccionario.agregarPalabra()
miDiccionario.agregarPalabra()
miDiccionario.agregarPalabra()
input("Presione enter para continuar...")
pal = input("Ingrese la palabra en español que desea consultar: ").upper()
miDiccionario.consultarEspaniolToIngles(pal)
miDiccionario.listarPalabras()
input("Presione enter para continuar...")
miDiccionario.consultarEspaniolToIngles(pal)
