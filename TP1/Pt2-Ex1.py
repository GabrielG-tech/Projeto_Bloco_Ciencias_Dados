import time
import re

# Função para extrair números de uma string
def extract_number(file_name):
    return [int(num) for num in re.findall(r'\d+', file_name)]

def bubble_sort(data):
    n = len(data)
    for i in range(n):
        for j in range(0, n - i - 1):
            if extract_number(data[j]) > extract_number(data[j + 1]):
                data[j], data[j + 1] = data[j + 1], data[j]

def selection_sort(data):
    n = len(data)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if extract_number(data[j]) < extract_number(data[min_idx]):
                min_idx = j
        data[i], data[min_idx] = data[min_idx], data[i]

def insertion_sort(data):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        while j >= 0 and extract_number(key) < extract_number(data[j]):
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key

def time_counter(sort_function, data):
    tempo_inicial = time.time()
    sort_function(data)
    return time.time() - tempo_inicial

with open("listagem_arquivos.txt", "r") as arquivo:
    lines = arquivo.readlines()

data = [line.strip() for line in lines]

# Bubble Sort
data_copy = data.copy()
tempo_bubble_sort = time_counter(bubble_sort, data_copy)
print(f"Bubble Sort: {tempo_bubble_sort:.6f} segundos")

# Selection Sort
data_copy = data.copy()
tempo_selection_sort = time_counter(selection_sort, data_copy)
print(f"Selection Sort: {tempo_selection_sort:.6f} segundos")

# Insertion Sort
data_copy = data.copy()
tempo_insertion_sort = time_counter(insertion_sort, data_copy)
print(f"Insertion Sort: {tempo_insertion_sort:.6f} segundos")

