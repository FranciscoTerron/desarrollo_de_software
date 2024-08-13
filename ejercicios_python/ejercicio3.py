def suma(n,m):
    return n + m

def multiplicacion(n,m):
    return n*m

def division(n,m):
    return n/m

def resta(n,m):
    return n - m 

# Funcion para el menu
def menu (opcion):
    if(opcion == 1):
        print("La sumatoria es"+ " " + str(suma(n1,n2)))
    elif(opcion == 2):
       print("La resta es" + " " +str(resta(n1,n2)))
    elif(opcion == 3):
        print("La multiplicacion es" + " " +str(multiplicacion(n1,n2)))
    elif(opcion == 4):
       print("La division es" + " "+  str(division(n1,n2)))
    else:
        print("Valor ingresado no valido")


n1 = int(input("Ingrese el primer valor:\n"))
n2 = int(input("Ingrese el segundo valor:\n"))
opcion = int(input("Ingrese 1 para sumar, 2 para restar , 3 para multiplicar, 4 para dividir\n"))
menu(opcion)



