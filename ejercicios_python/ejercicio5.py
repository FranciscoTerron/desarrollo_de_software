def obtenerDatosPeliculas (peliculas):
    i = 0;
    for i in range(5):
        nombre = input("Ingrese el nombre de la pelicula: ")
        anio = input("Ingrese el año de la pelicula:  ")
        pelicula = {"anio":anio,"nombre":nombre}
        peliculas.append(pelicula)
    
    return peliculas


def ordenarPeliculas (peliculas):
    peliculas.sort(key=lambda pelicula: pelicula['nombre'])
    i = 0
    for i in range(5):
        print("Pelicula : ", peliculas[i]['nombre'])
    


#Utilizo el ejercicio
peliculas = []
obtenerDatosPeliculas(peliculas)
ordenarPeliculas(peliculas)
    
    
   
    
    
    
