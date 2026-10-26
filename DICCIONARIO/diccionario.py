from palabra import Palabra

class Diccionario():
    
    def __init__(self):
        self.listaPalabras = []
        
    def agregarPalabra(self):
        espaniol = input("Ingrese la palabra en español: ").upper()
        ingles = input("Ingrese la palabra en inglés: ").upper()
        
        #Crear el objeto palabra
        unaPalabra = Palabra(espaniol, ingles)
        self.listaPalabras.append(unaPalabra)
        input("Palabra agregada correctamente, presione enter para continuar...")
        
    def consultarEspaniolToIngles(self, espaniol):
        """_summary_
Funcion para consultar una palabra en español y mostrar su traducción al inglés
        Args:
            espaniol (_type_): _description_
        """
        #Buscar la palabra en español en la lista de palabras
        
        for palabra in self.listaPalabras:
            if palabra.espaniol == espaniol:
                print(f"La palabra {espaniol} en inglés es: {palabra.ingles}")
                break
            else:
                print(f"La palabra {espaniol} no se encuentra en el diccionario")
                
            input ("Presione enter para continuar...")
            
    def listarPalabras(self):
        for palabra in self.listaPalabras:
            print(f"{palabra.espaniol} => {palabra.ingles}")
            
      