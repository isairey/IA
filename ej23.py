def heuristica(a, b):
    return abs(a - b)

objetivo = 50
valores = [20 ,35, 55, 60, 70]

mejor_valor = min(valores, key=lambda x:heuristica(x, objetivo))
print(f"El valor mas cercano al objetivo {objetivo} es : {mejor_valor}")