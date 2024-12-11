def bellman_ford(grafo, inicio):
    distancias = {vertice: float('inf') for vertice in grafo}
    distancias[inicio] = 0
    nos_anteriores = {vertice: None for vertice in grafo}

    # relaxa as arestas |V|-1 vezes
    for _ in range(len(grafo) - 1):
        for vertice in grafo:
            for vizinho, peso in grafo[vertice].items():
                if distancias[vertice] + peso < distancias[vizinho]:
                    distancias[vizinho] = distancias[vertice] + peso
                    nos_anteriores[vizinho] = vertice

    # verificar ciclos negativos
    for vertice in grafo:
        for vizinho, peso in grafo[vertice].items():
            if distancias[vertice] + peso < distancias[vizinho]:
                raise ValueError("O grafo contém um ciclo negativo.")

    return distancias, nos_anteriores

# ex grafo com pesos negativos
grafo = {
    'A': {'B': -1, 'C': 4},
    'B': {'C': 3, 'D': 2, 'E': 2},
    'C': {},
    'D': {'B': 1, 'C': 5},
    'E': {'D': -3}
}

no_inicial = 'A'

try:
    distancias, caminhos = bellman_ford(grafo, no_inicial)
    print("Distâncias mínimas:", distancias)
    print("Caminhos:", caminhos)
except ValueError as e:
    print(e)
