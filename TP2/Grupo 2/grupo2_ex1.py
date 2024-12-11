def quicksort(arr):
    # se a lista tiver 1 ou 0 elementos, está ordenada
    if len(arr) <= 1:
        return arr
    else:
        # escolhe o pivô (último elemento)
        pivo = arr[-1]
        
        # divide a lista em dois sub-arrays (menor que o pivô e maior que o pivô)
        menor = [x for x in arr[:-1] if x <= pivo]
        maior = [x for x in arr[:-1] if x > pivo]
        
        # recursivamente ordena os sub-arrays e concatena com o pivô no meio
        return quicksort(menor) + [pivo] + quicksort(maior)

lista = [34, 7, 23, 32, 5, 62]
print(f"Lista original: {lista}")
lista_ordenada = quicksort(lista)
print(f"Lista ordenada: {lista_ordenada}")
