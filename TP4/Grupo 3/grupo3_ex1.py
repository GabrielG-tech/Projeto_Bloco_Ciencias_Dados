class Grafo:
    def __init__(self):
        self.grafo = {}

    def add_aresta(self, u, v):
        # adiciona uma aresta entre os vértices u e v
        if u not in self.grafo:
            self.grafo[u] = []
        if v not in self.grafo:
            self.grafo[v] = []
        self.grafo[u].append(v)
        self.grafo[v].append(u)

    def dfs(self, inicio):
        # busca em profundidade (DFS)
        visitados = set()
        resultado = []
        
        def dfs_recursivo(no):
            visitados.add(no)
            resultado.append(no)
            for vizinho in self.grafo.get(no, []):
                if vizinho not in visitados:
                    dfs_recursivo(vizinho)

        dfs_recursivo(inicio)
        return resultado

    def bfs(self, inicio):
        # busca em largura (BFS)
        visitados = set()
        queue = [inicio]
        resultado = []

        visitados.add(inicio)
        while queue:
            no = queue.pop(0)
            resultado.append(no)
            for vizinho in self.grafo.get(no, []):
                if vizinho not in visitados:
                    visitados.add(vizinho)
                    queue.append(vizinho)

        return resultado

    def esta_conectado(self):
        # verifica se o grafo é conexo (usando DFS)
        if not self.grafo:
            return True
        no_inicial = next(iter(self.grafo))
        visitados = set()
        
        def dfs(no):
            visitados.add(no)
            for vizinho in self.grafo.get(no, []):
                if vizinho not in visitados:
                    dfs(vizinho)

        dfs(no_inicial)
        return len(visitados) == len(self.grafo)

    def contar_componentes_conectados(self):
        # conta o número de componentes conectados no grafo
        visitados = set()
        componentes = 0

        def dfs(no):
            visitados.add(no)
            for vizinho in self.grafo.get(no, []):
                if vizinho not in visitados:
                    dfs(vizinho)

        for no in self.grafo:
            if no not in visitados:
                dfs(no)
                componentes += 1

        return componentes

grafo = Grafo()
grafo.add_aresta(1, 2)
grafo.add_aresta(1, 3)
grafo.add_aresta(2, 4)
grafo.add_aresta(3, 5)

# DFS
print("DFS:", grafo.dfs(1))

# BFS
print("BFS:", grafo.bfs(1))

# Verificar se o grafo é conexo
print("Grafo é conexo:", grafo.esta_conectado()) 

# Contar componentes conectados
grafo2 = Grafo()
grafo2.add_aresta(1, 2)
grafo2.add_aresta(3, 4)
print("Componentes conectados:", grafo2.contar_componentes_conectados()) 
