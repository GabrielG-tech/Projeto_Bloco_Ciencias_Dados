from concurrent.futures import ThreadPoolExecutor

# definindo a estrutura de um nó de árvore binária de busca
class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

# insere um valor na árvore binária de busca
def inserir(no, valor):
    if no is None:
        return No(valor)
    if valor < no.valor:
        no.esquerda = inserir(no.esquerda, valor)
    else:
        no.direita = inserir(no.direita, valor)
    return no

# busca sequencial
def buscar_sequencial(no, valor):
    if no is None:
        return False
    if no.valor == valor:
        return True
    elif valor < no.valor:
        return buscar_sequencial(no.esquerda, valor)
    else:
        return buscar_sequencial(no.direita, valor)

# busca paralela utilizando ThreadPoolExecutor
def buscar_paralela(no, valor):
    if no is None:
        return False
    
    # se o valor for igual ao valor do no valor já encontrado
    if no.valor == valor:
        return True

    # criar um pool de threads para procurar nas subárvores paralelamente
    with ThreadPoolExecutor() as executor:
        # as tarefas paralelizadas
        futuras = []
        if valor < no.valor:
            futuras.append(executor.submit(buscar_paralela, no.esquerda, valor))
        else:
            futuras.append(executor.submit(buscar_paralela, no.direita, valor))

        # esperar pela conclusão de todas as tarefas
        for futura in futuras:
            if futura.result():
                return True
    return False

raiz = No(10)
raiz = inserir(raiz, 5)
raiz = inserir(raiz, 15)
raiz = inserir(raiz, 2)
raiz = inserir(raiz, 7)
raiz = inserir(raiz, 12)
raiz = inserir(raiz, 18)

valor_busca = 7
resultado_sequencial = buscar_sequencial(raiz, valor_busca)
print(f"Valor {valor_busca} encontrado (Busca Sequencial): {resultado_sequencial}")

resultado_paralelo = buscar_paralela(raiz, valor_busca)
print(f"Valor {valor_busca} encontrado (Busca Paralela): {resultado_paralelo}")
