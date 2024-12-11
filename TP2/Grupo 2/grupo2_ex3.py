import random
import time

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivo = arr[-1]
    menor = [x for x in arr[:-1] if x <= pivo]
    maior = [x for x in arr[:-1] if x > pivo]
    return quicksort(menor) + [pivo] + quicksort(maior)

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    meio = len(arr) // 2
    esquerda = merge_sort(arr[:meio])
    direita = merge_sort(arr[meio:])
    return merge(esquerda, direita)

def merge(esquerda, direita):
    resultado = []
    i = j = 0
    while i < len(esquerda) and j < len(direita):
        if esquerda[i] < direita[j]:
            resultado.append(esquerda[i])
            i += 1
        else:
            resultado.append(direita[j])
            j += 1
    resultado.extend(esquerda[i:])
    resultado.extend(direita[j:])
    return resultado

def comparar_algoritmos():
    tamanhos = [100, 1000, 5000, 10000, 50000]  # define tamanhos das listas para teste
    for tamanho in tamanhos:
        # cria lista de nums aleatórios para cada tamanho
        lista = random.sample(range(1, 100000), tamanho)
        
        # teste do QuickSort
        lista_quick = lista.copy()
        start = time.time()
        quicksort(lista_quick)
        tempo_quick = time.time() - start
        
        # teste do Bubble Sort
        lista_bubble = lista.copy()
        start = time.time()
        bubble_sort(lista_bubble)
        tempo_bubble = time.time() - start
        
        # teste do Merge Sort
        lista_merge = lista.copy()
        start = time.time()
        merge_sort(lista_merge)
        tempo_merge = time.time() - start
        
        print(f"Tamanho da lista: {tamanho}")
        print(f"QuickSort: {tempo_quick:.6f} segundos")
        print(f"Bubble Sort: {tempo_bubble:.6f} segundos")
        print(f"Merge Sort: {tempo_merge:.6f} segundos")
        print("-" * 50)
comparar_algoritmos()
