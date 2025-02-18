def es_par(num):
    """Verifica si un numero es par"""
    return num % 2 == 0

def suma_de_pares(a,b):
    """Verifica si la suma de dos numeros es par"""
    if es_par(a) and es_par(b):
        suma = a + b
        return True, suma
    return False, None

print("Bienvenido a la demostracion del teorema: la suma de 2 numeros pares es siempre par")
numero2 = int(input("introduce el primer numero par"))
numero3 = int(input("introduce el Segundo numero par"))

if es_par(numero2) and es_par(numero3):
    es_suma_par , resultado = suma_de_pares(numero2,numero3)
    if es_suma_par:
        print(f"la suma de {numero2} y {numero3}  es {resultado} que es un numero par")
        
    else:
        print(f"Error la suma de {numero2} y {numero3} no es par")
        
else: 
    print("Al menos uno de los 2 numeros no es para segurate de ingresar los 2 numeros pares")