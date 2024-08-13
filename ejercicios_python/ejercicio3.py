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
        suma(n1,n2)
    elif(opcion == 2):
        multiplicacion(n1,n2)
    elif(opcion == 3):
        division(n1,n2)
    elif(opcion == 4):
        resta(n1,n2)
    else:
        print("Valor ingresado no valido")


n1 = print("Ingrese el primer valor")
n2 = print("Ingrese el segundo valor")
opcion = print("Ingrese 1 para sumar, 2 para restar , 3 para multiplicar, 4 para dividir")
menu(opcion)



