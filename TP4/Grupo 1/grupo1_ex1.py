import heapq

def criar_heap_min(lista):
    # transforma a lista em uma heap mínima
    heapq.heapify(lista)
    return lista

def menor_elemento(heap):
    # retorna o menor elemento da heap sem remover
    return heap[0] if heap else None

def criar_heap_max(lista):
    # transforma a lista em uma heap máxima (valores invertidos)
    return [-x for x in criar_heap_min([-i for i in lista])]

def inserir_heap_max(heap, elemento):
    # insere um elemento em uma heap máxima
    heapq.heappush(heap, -elemento)

def remover_maior_heap_max(heap):
    # remove o maior elemento de uma heap máxima
    return -heapq.heappop(heap)

def buscar_na_heap(heap, valor):
    # busca um valor na heap e retorna o índice ou -1 se não estiver presente
    try:
        return heap.index(valor)
    except ValueError:
        return -1

def heapsort(lista):
    # ordena uma lista de forma crescente usando heap
    heap = []
    for elemento in lista:
        heapq.heappush(heap, elemento)
    return [heapq.heappop(heap) for _ in range(len(heap))]

lista = [5, 1, 8, 3, 2]
heap_min = criar_heap_min(lista.copy())
print("Heap mínima:", heap_min)
print("Menor elemento:", menor_elemento(heap_min))

heap_max = criar_heap_max(lista.copy())
print("Heap máxima:", [-x for x in heap_max])
inserir_heap_max(heap_max, 10)
print("Heap máxima após inserir 10:", [-x for x in heap_max])
print("Maior removido:", remover_maior_heap_max(heap_max))

print("Busca 8 na heap mínima:", buscar_na_heap(heap_min, 8))
print("Heapsort:", heapsort(lista))
