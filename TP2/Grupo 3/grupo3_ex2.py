# nó da lista duplamente encadeada
class No:
    def __init__(self, dado):
        self.dado = dado  # o valor armazenado no nó
        self.proximo = None  # o próximo nó na lista
        self.anterior = None  # o nó anterior na lista

class ListaDuplamenteEncadeada:
    def __init__(self):
        self.head = None  # a head da lista, inicialmente é None
        self.tail = None  # a tail da lista, inicialmente é None

    # insere um elemento no início da lista
    def inserir_inicio(self, dado):
        novo_no = No(dado)
        if self.head is None:  # se a lista estiver vazia
            self.head = novo_no
            self.tail = novo_no  # a tail será o mesmo nó que a head
            return
        novo_no.proximo = self.head  # o próximo do novo nó será a head atual
        self.head.anterior = novo_no  # o anterior da head será o novo nó
        self.head = novo_no  # a head da lista agora é o novo nó

    # insere um elemento no final da lista
    def inserir_fim(self, dado):
        novo_no = No(dado)
        if self.tail is None:  # se a lista estiver vazia
            self.head = novo_no
            self.tail = novo_no
            return
        self.tail.proximo = novo_no  # o próximo da tail será o novo nó
        novo_no.anterior = self.tail  # o anterior do novo nó será a tail
        self.tail = novo_no  # a tail agora é o novo nó

    # remove um elemento da lista
    def remover(self, dado):
        if self.head is None:  # se a lista estiver vazia, não remove nada
            print("a lista está vazia.")
            return
        # procura o nó a ser removido
        atual = self.head
        while atual:
            if atual.dado == dado:
                if atual.anterior:  # se não for o primeiro nó
                    atual.anterior.proximo = atual.proximo
                if atual.proximo:  # se não for o último nó
                    atual.proximo.anterior = atual.anterior
                if atual == self.head:  # se for o primeiro nó
                    self.head = atual.proximo
                if atual == self.tail:  # se for o último nó
                    self.tail = atual.anterior
                print(f"elemento {dado} removido.")
                return
            atual = atual.proximo
        print(f"elemento {dado} não encontrado na lista.")

    # le todos os elementos da lista do início para o fim
    def ler_elementos_frente(self):
        if self.head is None:
            print("a lista está vazia.")
            return
        atual = self.head
        while atual:
            print(atual.dado, end=" <-> ")
            atual = atual.proximo
        print("None")  # indica o fim da lista

    # le todos os elementos da lista do fim para o início
    def ler_elementos_tras(self):
        if self.tail is None:
            print("a lista está vazia.")
            return
        atual = self.tail
        while atual:
            print(atual.dado, end=" <-> ")
            atual = atual.anterior
        print("None")  # final da lista

lista = ListaDuplamenteEncadeada()
lista.inserir_inicio(10)
lista.inserir_inicio(20)
lista.inserir_fim(30)
lista.inserir_fim(40)

print("lista do início para o fim:")
lista.ler_elementos_frente()

print("lista do fim para o início:")
lista.ler_elementos_tras()

lista.remover(20)  # remove o elemento 20

print("lista depois de remover o elemento 20 do início para o fim:")
lista.ler_elementos_frente()

print("lista depois de remover o elemento 20 do fim para o início:")
lista.ler_elementos_tras()
