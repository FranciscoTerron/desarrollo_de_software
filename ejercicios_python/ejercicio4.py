def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_a_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9
   
 


temperatura = float(input("Ingrese temperatura : ")) 
escala = (input("Ingrese escala: "))

if escala == "C":
    resultado = celsius_a_fahrenheit(temperatura)
    print(f"Resultado: {resultado:.1f}°F")
elif escala == "F":
    resultado = fahrenheit_a_celsius(temperatura)
    print(f"Resultado:{resultado:.1f}°F")
else:
    print("La escala ingresada no es valida")
