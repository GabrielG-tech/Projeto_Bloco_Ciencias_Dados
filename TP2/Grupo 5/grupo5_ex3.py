from concurrent.futures import ThreadPoolExecutor
from collections import Counter

# conta frequência de elementos em uma lista
def contar_frequencia(parte_lista):
    return Counter(parte_lista)

# divide lista em partes e conta as frequências em paralelo
def contar_elementos(lista):
    num_threads = 4  # número de threads para dividir a lista
    tamanho_parte = len(lista) // num_threads
    partes = [lista[i:i + tamanho_parte] for i in range(0, len(lista), tamanho_parte)]

    # usar ThreadPoolExecutor para contar as frequências em paralelo
    with ThreadPoolExecutor() as executor:
        resultados = executor.map(contar_frequencia, partes)
    
    # combina resultados das contagens parciais
    frequencias_totais = Counter()
    for resultado in resultados:
        frequencias_totais.update(resultado)

    return frequencias_totais

lista_grande = [1, 2, 3, 4, 5, 6, 1, 2, 1, 4, 3, 2, 6, 7, 8, 9] * 100000
frequencias = contar_elementos(lista_grande)
print(f"Frequência de elementos: {frequencias}")
