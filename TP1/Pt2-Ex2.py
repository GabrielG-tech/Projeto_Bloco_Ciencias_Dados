from collections import deque
import time

with open("listagem_arquivos.txt", "r") as arquivo:
    lines = arquivo.readlines()

data = [line.strip() for line in lines]

# Hashtable
hashtable = {i: data[i] for i in range(len(data))}
inicio = time.time()
primeiro = hashtable[0]
ultimo = hashtable[len(data) - 1]
fim = time.time()
print(f"Hashtable: Primeiro = {primeiro}, Último = {ultimo}, Tempo = {fim - inicio:.6f} segundos")

# Stack
stack = list(data)
inicio = time.time()
stack.append("novo_arquivo.txt")
stack.pop()
fim = time.time()
print(f"Stack: Tempo = {fim - inicio:.6f}s")

# Queue
queue = deque(data)
inicio = time.time()
queue.append("novo_arquivo.txt")
queue.popleft()
fim = time.time()
print(f"Queue: Tempo = {fim - inicio:.6f}s")
