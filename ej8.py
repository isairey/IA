import datetime
nombre = str(input("Ingresa tu Nombre "))
fecha = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(f"Nombre del Cliente ",{nombre}," y la Fecha y Hora ",{fecha})