import heapq

def dijkstra(grafo, inicio):
    distancias = {vertice: float('inf') for vertice in grafo}
    distancias[inicio] = 0
    fila_prioridade = [(0, inicio)]  # (distância, nó)
    nos_anteriores = {vertice: None for vertice in grafo}

    while fila_prioridade:
        distancia_atual, vertice_atual = heapq.heappop(fila_prioridade)

        # ignora se já tiver uma distância menor
        if distancia_atual > distancias[vertice_atual]:
            continue

        for vizinho, peso in grafo[vertice_atual].items():
            distancia = distancia_atual + peso

            # atualiza se encontrar um caminho mais curto
            if distancia < distancias[vizinho]:
                distancias[vizinho] = distancia
                nos_anteriores[vizinho] = vertice_atual
                heapq.heappush(fila_prioridade, (distancia, vizinho))

    return distancias, nos_anteriores

grafo = {
    'A': {'B': 4, 'C': 1},
    'B': {'A': 4, 'C': 2, 'D': 5},
    'C': {'A': 1, 'B': 2, 'D': 8},
    'D': {'B': 5, 'C': 8}
}

no_inicial = 'A'
distancias, caminhos = dijkstra(grafo, no_inicial)

print("Distâncias mínimas:", distancias)
print("Caminhos:", caminhos)
