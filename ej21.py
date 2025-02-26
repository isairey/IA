opciones = ["ir al cine", "estudiar","hacer ejercicio"]
def tomar_decicion(prioridades):
    for opcion in opciones:
        if opcion in prioridades:
            return f"El agente decide : {opcion}"
    return f"El agente no decide nada."
prioridades = ["hacer ejercicio", "estudiar"]
print(tomar_decicion(prioridades))
    