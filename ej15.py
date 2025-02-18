datos_temperatura = {
    "madrugada": 10,
    "manana": 20,
    "medio dia": 35,
    "tarde": 25,
    "tardenoche": 20,
    "noche": 15
}

# El sistema hace predicciones de temperatura basándose en la observación
def predecir_temperatura(hora):
    if hora >=1 and hora<=5:
        return datos_temperatura["madrugada"]
    elif hora >5 and hora<11:
        return datos_temperatura["manana"]
    elif hora >=11 and hora<=12:
        return datos_temperatura["medio dia"]
    elif hora >=13 and hora<=17:
        return datos_temperatura["tarde"]
    elif hora >=17 and hora<=19:
        return datos_temperatura["tardenoche"]
    elif hora >19 and hora<24:
        return datos_temperatura["noche"]
    else:
        return "Hora no válida"

# Ejemplo de usos
hora = int(input("Ingresa la hora del dia: "))
print(f"La temperatura promedio en la {hora} es: {predecir_temperatura(hora)}°C")