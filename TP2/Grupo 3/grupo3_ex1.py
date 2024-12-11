# definindo o nó da lista encadeada
class No:
    def __init__(self, dado):
        self.dado = dado  # valor armazenado no nó
        self.proximo = None  # próximo nó na lista

# definindo a classe lista encadeada
class ListaEncadeada:
    def __init__(self):
        self.cabeca = None  # a cabeça da lista, inicialmente é None

    # insere um elemento no início da lista
    def inserir_inicio(self, dado):
        novo_no = No(dado)
        novo_no.proximo = self.cabeca  # o próximo do novo nó é o que era o início
        self.cabeca = novo_no  # a cabeça agora é o novo nó

    # insere um elemento no final da lista
    def inserir_fim(self, dado):
        novo_no = No(dado)
        if self.cabeca is None:  # se a lista estiver vazia, o novo nó se torna a cabeça
            self.cabeca = novo_no
            return
        # se a lista não estiver vazia, percorre até o último nó
        atual = self.cabeca
        while atual.proximo:
            atual = atual.proximo
        atual.proximo = novo_no  # o último nó aponta para o novo nó

    # remove um elemento da lista
    def remover(self, dado):
        if self.cabeca is None:  # se a lista estiver vazia, não pode remover nada
            print("a lista está vazia.")
            return
        # se o elemento a ser removido é o primeiro
        if self.cabeca.dado == dado:
            self.cabeca = self.cabeca.proximo  # a cabeça aponta para o próximo nó
            return
        # caso não percorre a lista para encontrar o nó a ser removido
        atual = self.cabeca
        while atual.proximo:
            if atual.proximo.dado == dado:
                atual.proximo = atual.proximo.proximo  # remove o nó
                return
            atual = atual.proximo
        print(f"elemento {dado} não encontrado na lista.")

    # le todos os elementos da lista
    def ler_elementos(self):
        if self.cabeca is None:
            print("a lista está vazia.")
            return
        atual = self.cabeca
        while atual:
            print(atual.dado, end=" -> ")
            atual = atual.proximo
        print("None")  # fim da lista

lista = ListaEncadeada()
lista.inserir_inicio(10)
lista.inserir_inicio(20)
lista.inserir_fim(30)
lista.inserir_fim(40)

print("lista antes de remover o elemento 20:")
lista.ler_elementos()

# remove o elemento 20
lista.remover(20)  

print("lista depois de remover o elemento 20:")
lista.ler_elementos()
