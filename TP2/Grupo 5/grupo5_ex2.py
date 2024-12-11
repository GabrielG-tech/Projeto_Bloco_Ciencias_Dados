from concurrent.futures import ThreadPoolExecutor

# estrutura de um nó da árvore
class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

# insere um valor na árvore binária de busca
def inserir(nodo, valor):
    if nodo is None:
        return No(valor)
    if valor < nodo.valor:
        nodo.esquerda = inserir(nodo.esquerda, valor)
    else:
        nodo.direita = inserir(nodo.direita, valor)
    return nodo

# insere elementos em uma lista
def inserir_lista(lista, valor):
    lista.append(valor)

# remove um valor de uma árvore binária de busca
def remover(nodo, valor):
    if nodo is None:
        return nodo
    if valor < nodo.valor:
        nodo.esquerda = remover(nodo.esquerda, valor)
    elif valor > nodo.valor:
        nodo.direita = remover(nodo.direita, valor)
    else:
        if nodo.esquerda is None:
            return nodo.direita
        elif nodo.direita is None:
            return nodo.esquerda
        # caso o nó tenha ambos os filhos
        temp = nodo.direita
        while temp.esquerda:
            temp = temp.esquerda
        nodo.valor = temp.valor
        nodo.direita = remover(nodo.direita, temp.valor)
    return nodo

# temove um valor de uma lista
def remover_lista(lista, valor):
    if valor in lista:
        lista.remove(valor)

# executa operações paralelamente em uma árvore e lista
def realizar_operacoes():
    lista = []
    raiz = No(10)
    valores_lista = [1, 2, 3, 4, 5]
    valores_arvore = [7, 3, 1, 5, 9]

    # usa ThreadPoolExecutor para realizar operações em paralelo
    with ThreadPoolExecutor() as executor:
        # inserindo valores na lista e árvore em paralelo
        executor.submit(lambda: [inserir_lista(lista, v) for v in valores_lista])
        executor.submit(lambda: [inserir(raiz, v) for v in valores_arvore])
        
        # removendo valores na lista e árvore em paralelo
        executor.submit(lambda: [remover_lista(lista, v) for v in [2, 4]])
        executor.submit(lambda: [remover(raiz, v) for v in [3, 9]])

    print(f"Lista após operações: {lista}")
    print(f"Árvore após operações (valor da raiz): {raiz.valor}")
realizar_operacoes()
