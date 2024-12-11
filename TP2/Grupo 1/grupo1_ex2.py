import asyncio
import random   

# função assíncrona que simula uma tarefa com duração variável
async def tarefa_simulada(id_tarefa):
    # escolhe um tempo aleatório entre 1 e 5 segundos
    duracao = random.randint(1, 5)
    print(f"Tarefa {id_tarefa} iniciada e levará {duracao} segundos para concluir.")
    
    # aguarda pelo tempo definido anteriormente (simulção da tarefa)
    await asyncio.sleep(duracao)
    
    print(f"Tarefa {id_tarefa} concluída após {duracao} segundos.")

async def main():
    # lista para armazenar as tarefas a serem executadas
    tarefas = []
    
    # cria 5 tarefas simuladas e adiciona na lista
    for i in range(1, 6):
        tarefas.append(tarefa_simulada(i))
    
    # executa todas as tarefas em paralelo
    await asyncio.gather(*tarefas)

# inicia o loop de eventos assíncronos e executa a função main()
asyncio.run(main())
