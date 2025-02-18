datos_temperatura = {
    "Ciudad de México": 18,
    "Monterrey": 21,
    "Guadalajara": 19,
    "Cancún": 20,
    "Tijuana": 17,
    "Chihuahua": 15,
    "Tlaxiaco":16,
    "Toluca": 22,
}
hora = float(input("Ingresa la hora del dia: "))

ciudad_encontrada = None
for ciudad, temperatura in datos_temperatura.items():
    if hora == temperatura:
        ciudad_encontrada = ciudad
        break

if ciudad_encontrada:
    print(f"La temperatura de {datos_temperatura}°C corresponde a {ciudad_encontrada}.")
else:
    print("No existe una ciudad con esa temperatura en la lista.")

print(f"{datos_temperatura.items()}")