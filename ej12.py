#Isai Reyes Peña
def case_example(opcion):
    # Definir las opciones posibles en un diccionario
    cases = {
        1: "Has elegido la opción 1",
        2: "Has elegido la opción 2",
        3: "Has elegido la opción 3",
        'default': "Opción no válida"
    }
    
    # Obtener el mensaje correspondiente a la opción seleccionada
    return cases.get(opcion, cases['default'])

# Prueba del programa
opcion = int(input("Elige una opción (1, 2, 3): "))
print(case_example(opcion))
