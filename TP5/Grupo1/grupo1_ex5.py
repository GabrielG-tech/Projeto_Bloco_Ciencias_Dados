def encontrar(pais, vertice):
    # encontra a raiz do conjunto e aplica compressão de caminho
    if pais[vertice] != vertice:
        pais[vertice] = encontrar(pais, pais[vertice])
    return pais[vertice]

def unir(pais, rank, vertice1, vertice2):
    # une 2 conjuntos usando união por rank
    raiz1 = encontrar(pais, vertice1)
    raiz2 = encontrar(pais, vertice2)

    if rank[raiz1] > rank[raiz2]:
        pais[raiz2] = raiz1
    elif rank[raiz1] < rank[raiz2]:
        pais[raiz1] = raiz2
    else:
        pais[raiz2] = raiz1
        rank[raiz1] += 1

def kruskal(arestas, vertices):
    # ordena as arestas pelo peso
    arestas.sort()
    pais = {vertice: vertice for vertice in vertices}
    rank = {vertice: 0 for vertice in vertices}
    arvore_geradora = []
    peso_total = 0

    for peso, no1, no2 in arestas:
        if encontrar(pais, no1) != encontrar(pais, no2):
            unir(pais, rank, no1, no2)
            arvore_geradora.append((no1, no2, peso))
            peso_total += peso

    return arvore_geradora, peso_total

# Lista de arestas (peso, nó1, nó2)
arestas = [
    (2, 'A', 'B'),
    (3, 'A', 'C'),
    (1, 'B', 'C'),
    (4, 'B', 'D'),
    (5, 'C', 'D')
]

vertices = {'A', 'B', 'C', 'D'}

arvore_geradora, peso_total = kruskal(arestas, vertices)

print("Arestas da Árvore Geradora Mínima:")
for aresta in arvore_geradora:
    print(f"{aresta[0]} - {aresta[1]} (peso: {aresta[2]})")

print(f"Peso total da árvore geradora mínima: {peso_total}")
