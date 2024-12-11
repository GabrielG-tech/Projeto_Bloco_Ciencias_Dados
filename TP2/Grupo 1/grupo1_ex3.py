import concurrent.futures
import math

def verifica_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(math.sqrt(numero)) + 1):
        if numero % i == 0:
            return False
    return True

# calcular num primos dentro de um intervalo
def calcula_intervalos_primos(inicio, fim):
    primos = []
    for num in range(inicio, fim):
        if verifica_primo(num):
            primos.append(num)
    return primos

# intervalo de números para verificar primos
limite_superior = 100000
num_threads = 4  # num de threads para executar em paralelo

# divide o trabalho entre os núcleos disponíveis
intervalo = limite_superior // num_threads
tarefas = []

# cria um pool de threads para executar a tarefa em paralelo
with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
    # divide o intervalo de trabalho de cada thread
    for i in range(num_threads):
        inicio = i * intervalo
        fim = (i + 1) * intervalo if i != num_threads - 1 else limite_superior
        # executa as tarefas em paralelo
        tarefas.append(executor.submit(calcula_intervalos_primos, inicio, fim))
    
    # aguarda todas as tarefas terminarem e coleta os resultados
    primos_totais = []
    for tarefa in concurrent.futures.as_completed(tarefas):
        primos_totais.extend(tarefa.result())

print(f"Números primos encontrados: {len(primos_totais)}")
print(f"Exemplo de números primos: {primos_totais[:10]}...")

