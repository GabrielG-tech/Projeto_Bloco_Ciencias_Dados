import heapq

def prim(grafo):
    # seleciona o 1º vértice arbitrário
    inicio = next(iter(grafo))
    visitados = set()
    fila_prioridade = [(0, inicio, None)]  # (peso, nó_atual, nó_anterior)
    arvore_geradora = []
    peso_total = 0

    while fila_prioridade:
        peso, no_atual, no_anterior = heapq.heappop(fila_prioridade)

        # ignora se o nó já foi visitado
        if no_atual in visitados:
            continue

        # marca como visitado
        visitados.add(no_atual)

        # add a aresta à árvore geradora, exceto para o 1º nó
        if no_anterior is not None:
            arvore_geradora.append((no_anterior, no_atual, peso))
            peso_total += peso

        # adiciona vizinhos à fila de prioridade
        for vizinho, peso_vizinho in grafo[no_atual].items():
            if vizinho not in visitados:
                heapq.heappush(fila_prioridade, (peso_vizinho, vizinho, no_atual))

    return arvore_geradora, peso_total

grafo = {
    'A': {'B': 2, 'C': 3},
    'B': {'A': 2, 'C': 1, 'D': 4},
    'C': {'A': 3, 'B': 1, 'D': 5},
    'D': {'B': 4, 'C': 5}
}

arvore_geradora, peso_total = prim(grafo)

print("Arestas da Árvore Geradora Mínima:")
for aresta in arvore_geradora:
    print(f"{aresta[0]} - {aresta[1]} (peso: {aresta[2]})")

print(f"Peso total da árvore geradora mínima: {peso_total}")
