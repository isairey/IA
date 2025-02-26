import runpy
def interactuar():
    print("Bienvenido al sistema de Ejecicios en Clase")
    while True:
        print("\n Elige una Opcion")
        print("1.- Suma de 2 Numeros")
        print("2.- Datos de la carrera")
        print("3.- Multiplicacion y Resta de 2 Numeros")
        print("4.- Numero par")
        print("5.- Numero Positivo o Negativo")
        print("6.- Numero Aleatorio")
        print("7.- Calificacion entre 1 y 100")
        print("8.- Funcion DataTime")
        print("9.- Total de Compra")
        print("10.- Descuento de Compra")
        print("11.- Tiket de Tienda")
        print("12.- Ejemplo Case")
        print("13.- Case con For")
        print("14.- Numero par e Impar")
        print("15.- Temperatura con Arreglos")
        print("16.- Temperatura de ciudades")
        print("17.- Temperatura con Ciudades Mejorado")
        print("18.- Ejemplo de For")
        print("19.- Nodos")
        print("20.- Numeros Pares e Impares")
        print("21.- Ejercicio de Agente ")
        print("22.- Agente con Ubicaciones")
        print("23.- Heuristica")
        print("24.- Grafos")
        print("25.- Grafos por DFS ")
        print("26.- Ruta mas corta de Grafos")
        print("27.- Solucion optima")
        print("28.- Salir")
        opcion = input("Selecciona una opcion : ")
        
        if opcion == "1":
            runpy.run_path("ej1.py")
        elif opcion == "2":
            runpy.run_path("ej2.py") 
        elif opcion == "3":
            runpy.run_path("ej3.py")
        elif opcion == "4":
            runpy.run_path("ej4.py")
        elif opcion == "5":
            runpy.run_path("ej5.py") 
        elif opcion == "6":
            runpy.run_path("ej6.py")
        elif opcion == "7":
            runpy.run_path("ej7.py")
        elif opcion == "8":
            runpy.run_path("ej8.py") 
        elif opcion == "9":
            runpy.run_path("ej9.py")
        elif opcion == "10":
            runpy.run_path("ej10.py")
        elif opcion == "11":
            runpy.run_path("ej11.py") 
        elif opcion == "12":
            runpy.run_path("ej12.py")
        elif opcion == "13":
            runpy.run_path("ej13.py")
        elif opcion == "14":
            runpy.run_path("ej14.py") 
        elif opcion == "15":
            runpy.run_path("ej15.py")
        elif opcion == "16":
            runpy.run_path("ej16.py")
        elif opcion == "17":
            runpy.run_path("ej17.py") 
        elif opcion == "18":
            runpy.run_path("ej18.py")
        elif opcion == "19":
            runpy.run_path("ej19.py")
        elif opcion == "20":
            runpy.run_path("ej20.py") 
        elif opcion == "21":
            runpy.run_path("ej21.py")
        elif opcion == "22":
            runpy.run_path("ej22.py")
        elif opcion == "23":
            runpy.run_path("ej23.py") 
        elif opcion == "24":
            runpy.run_path("ej24.py")
        elif opcion == "25":
            runpy.run_path("ej25.py")
        elif opcion == "26":
            runpy.run_path("ej26.py") 
        elif opcion == "27":
            runpy.run_path("ej27.py")
        elif opcion == "28":
            break
        else:
            print("Esta opcion no es Valida")
interactuar()
        
        
        
        
