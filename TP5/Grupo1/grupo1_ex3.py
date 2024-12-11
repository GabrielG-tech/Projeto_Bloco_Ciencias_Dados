def floyd_warshall(grafo):
    # matriz de distâncias
    vertices = list(grafo.keys())
    n = len(vertices)
    matriz_distancias = {v: {u: float('inf') for u in vertices} for v in vertices}

    # define a distância para si mesmo igual a 0
    for vertice in vertices:
        matriz_distancias[vertice][vertice] = 0

    # preenche as distâncias iniciais com base no grafo
    for vertice in grafo:
        for vizinho, peso in grafo[vertice].items():
            matriz_distancias[vertice][vizinho] = peso

    # atualiza as distâncias usando vértices intermediários
    for k in vertices:
        for i in vertices:
            for j in vertices:
                matriz_distancias[i][j] = min(
                    matriz_distancias[i][j],
                    matriz_distancias[i][k] + matriz_distancias[k][j]
                )

    return matriz_distancias

grafo = {
    'A': {'B': 3, 'C': 8, 'E': -4},
    'B': {'D': 1, 'E': 7},
    'C': {'B': 4},
    'D': {'A': 2, 'C': -5},
    'E': {'D': 6}
}

matriz_distancias = floyd_warshall(grafo)

print("Matriz de distâncias mínimas:")
for origem, destinos in matriz_distancias.items():
    print(f"{origem}: {destinos}")
