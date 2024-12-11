def quickselect(arr, k):
    # se a lista tiver apenas um elemento, retorna esse elemento
    if len(arr) == 1:
        return arr[0]
    
    # escolhe o pivô, que é o último elemento da lista
    pivo = arr[-1]
    
    # divide a lista em dois sub-arrays
    menor = [x for x in arr[:-1] if x <= pivo]
    maior = [x for x in arr[:-1] if x > pivo]
    
    # verificação de onde está o k-ésimo elemento
    if len(menor) == k:
        return pivo  # O pivô é o k-ésimo menor elemento
    elif len(menor) > k:
        # k-ésimo menor elemento está na sub-array "menor"
        return quickselect(menor, k)
    else:
        # k-ésimo menor elemento está na sub-array "maior"
        return quickselect(maior, k - len(menor) - 1)

lista = [34, 7, 23, 32, 5, 62]
k = 3
print(f"A lista original: {lista}")
resultado = quickselect(lista, k)
print(f"O {k}-ésimo menor elemento é: {resultado}")
