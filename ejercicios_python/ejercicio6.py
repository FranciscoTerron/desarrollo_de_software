#Importo datetime para trabajar con fechas
from datetime import datetime

class Libro:
    def __init__(self,titulo,autor,año,genero):
        self.titulo = titulo
        self.autor = autor
        self.año = año
        self.genero = genero
        
    # Funcion para devolver la informacion del libro    
    def obtenerInfo(self):
        return f"La informacion del libro es -> Titulo: {self.titulo}  Autor: {self.autor}  Año: {self.año}  Genero: {self.genero}"
    
    def esClasico(self):
        # Resto el año actual por el del libro para obtener la diferencia
        if(( datetime.now().year - self.año) > 50):
            return True
        else:
            return False
    
    
#Pruebo la clase 

l1 = Libro("Martin Fierro","Juan", 1990, 'M')
l2 = Libro("PanchoLibro","Pedro",1970,"M")

print(l1.obtenerInfo())
print(l2.obtenerInfo())

print(l1.esClasico())
print(l2.esClasico()) 
  
  