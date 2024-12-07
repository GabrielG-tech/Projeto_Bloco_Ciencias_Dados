import time

def bubble_sort(data):
    n = len(data)
    for i in range(n):
        for j in range(0, n - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]

def selection_sort(data):
    n = len(data)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if data[j] < data[min_idx]:
                min_idx = j
        data[i], data[min_idx] = data[min_idx], data[i]

def insertion_sort(data):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        while j >= 0 and key < data[j]:
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

for sort_name, sort_function in [("Bubble Sort", bubble_sort), 
                                    ("Selection Sort", selection_sort), 
                                    ("Insertion Sort", insertion_sort)]:
    data_copy = data.copy()
    tempo = time_counter(sort_function, data_copy)
    print(f"{sort_name}: {tempo:.6f} segundos")
