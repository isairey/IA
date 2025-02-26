grafo = { 
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

def dfs(grafo, nodo,visitados=None):
    if visitados is None:
        visitados = set()
    visitados.add(nodo)
    for vecino in grafo[nodo]:
        if vecino not in visitados:
            dfs(grafo, vecino, visitados)
    return visitados

resultado = dfs(grafo, 'A')
print(f"Nodos Vissitados por DFS : {resultado}")