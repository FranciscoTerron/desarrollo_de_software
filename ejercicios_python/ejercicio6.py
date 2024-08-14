#Defino clase

class Libro:
    def __init__(self,titulo,autor,año,genero):
        self.titulo = titulo
        self.autor = autor
        self.año = año
        self.genero = genero
        
    def obtenerInfo(self):
        return f"La informacion del libro es -> Titulo: {self.titulo}  Autor: {self.autor}  Año: {self.año}  Genero: {self.genero}"
    
    
#Pruebo la clase 

l1 = Libro("Martin Fierro","Juan", 1990, 'M')


l1.obtenerInfo()
    