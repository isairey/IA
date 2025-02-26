from collections import deque
grafo = { 
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

def dfs(grafo, inicio):
    visitados = set()
    cola = deque([inicio])
    
    while cola:
        nodo = cola.popleft()
        if nodo not in visitados:
            visitados.add(nodo)
            for vecino in grafo[nodo]:
                if vecino not in visitados:
                    cola.append(vecino)
    return visitados

resultado = dfs(grafo, 'A')
print(f"Nodos Vissitados por DFS : {resultado}")