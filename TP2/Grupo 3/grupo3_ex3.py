# nó da lista encadeada
class No:
    def __init__(self, dado):
        self.dado = dado  # valor armazenado no nó
        self.proximo = None  # referência para o próximo nó

# classe para a lista encadeada
class ListaEncadeada:
    def __init__(self):
        self.cabeca = None  # a cabeça da lista, inicialmente é None

    # inserir um elemento no final da lista
    def inserir_fim(self, dado):
        novo_no = No(dado)
        if self.cabeca is None:  # se a lista estiver vazia
            self.cabeca = novo_no
            return
        atual = self.cabeca
        while atual.proximo:
            atual = atual.proximo
        atual.proximo = novo_no

    # mesclar duas listas encadeadas
    def mesclar(self, outra_lista):
        if self.cabeca is None:  # se a lista atual estiver vazia
            self.cabeca = outra_lista.cabeca
            return
        if outra_lista.cabeca is None:  # se a outra lista estiver vazia
            return
        # encontrar o último nó da lista atual
        atual = self.cabeca
        while atual.proximo:
            atual = atual.proximo
        # agora, conecta o último nó da lista atual ao primeiro nó da outra lista
        atual.proximo = outra_lista.cabeca

    # reverter a lista encadeada
    def reverter(self):
        anterior = None
        atual = self.cabeca
        while atual:
            proximo = atual.proximo  # armazena o próximo nó
            atual.proximo = anterior  # inverte o ponteiro
            anterior = atual  # move o ponteiro anterior para o nó atual
            atual = proximo  # move para o próximo nó
        self.cabeca = anterior  # a cabeça agora é o último nó

    # ler os elementos da lista
    def ler_elementos(self):
        if self.cabeca is None:
            print("a lista está vazia.")
            return
        atual = self.cabeca
        while atual:
            print(atual.dado, end=" -> ")
            atual = atual.proximo
        print("None")

lista1 = ListaEncadeada()
lista1.inserir_fim(10)
lista1.inserir_fim(20)
lista1.inserir_fim(30)

lista2 = ListaEncadeada()
lista2.inserir_fim(40)
lista2.inserir_fim(50)

print("lista 1 antes da mesclagem:")
lista1.ler_elementos()

print("lista 2 antes da mesclagem:")
lista2.ler_elementos()

lista1.mesclar(lista2)

print("lista 1 após mesclagem:")
lista1.ler_elementos()

lista1.reverter()

print("lista 1 após reversão:")
lista1.ler_elementos()
