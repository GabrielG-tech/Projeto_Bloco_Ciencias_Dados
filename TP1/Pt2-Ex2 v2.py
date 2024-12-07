from collections import deque
from memory_profiler import memory_usage
import time

# Lendo o arquivo de listagem
with open("listagem_arquivos.txt", "r") as arquivo:
    lines = arquivo.readlines()

data = [line.strip() for line in lines]

# Posições  (1, 100, 1000, 5000 e última)
posicoes = [1, 100, 1000, 5000, len(data) - 1]

# Função para medir desempenho (tempo e memória)
def medida_desempenho(func, *args):
    mem_antes = memory_usage(max_usage=True) # Medir memória antes
    tempo_inicio = time.time()
    resultado = func(*args)
    tempo_execucao = time.time() - tempo_inicio
    mem_depois = memory_usage(max_usage=True) # Medir memória depois
    mem_usada = mem_depois - mem_antes
    return tempo_execucao, mem_usada, resultado

def hashtable():
    hashtable = {i: data[i] for i in range(len(data))}
    resultados = [hashtable.get(pos, "Não existe") for pos in posicoes]
    return resultados

tempo_execucao, mem_usada, resultados = medida_desempenho(hashtable)
print("Hashtable:")
print(f"Arquivos nas posições solicitadas: {resultados}")
print(f"Tempo de execução: {tempo_execucao:.6f} segundos")
print(f"Memória usada: {mem_usada:.6f} MiB\n")

def stack():
    stack = list(data)
    stack.append("novo_arquivo.txt")  
    stack.pop()  
    resultados = [stack[pos] if pos < len(stack) else "Não existe" for pos in posicoes]
    return resultados

tempo_execucao, mem_usada, resultados = medida_desempenho(stack)
print("Stack:")
print(f"Arquivos nas posições solicitadas: {resultados}")
print(f"Tempo de execução: {tempo_execucao:.6f} segundos")
print(f"Memória usada: {mem_usada:.6f} MiB\n")

def queue():
    queue = deque(data)
    queue.append("novo_arquivo.txt")  
    queue.popleft()  
    resultados = [queue[pos] if pos < len(queue) else "Não existe" for pos in posicoes]
    return resultados

tempo_execucao, mem_usada, resultados = medida_desempenho(queue)
print("Queue:")
print(f"Arquivos nas posições solicitadas: {resultados}")
print(f"Tempo de execução: {tempo_execucao:.6f} segundos")
print(f"Memória usada: {mem_usada:.6f} MiB")
