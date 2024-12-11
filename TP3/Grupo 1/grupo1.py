import threading

class Node:
    def __init__(self, value):
        self.value = value  
        # ponteiros para o nó da esquerda e direita
        self.left = None    
        self.right = None   

class BinaryTree:
    def __init__(self):
        self.root = None 

    def insert(self, value):
        # se a árvore estiver vazia, o nó se torna a raiz
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, current, value):
        # se o valor for menor, o nó será inserido na subárvore esquerda
        if value < current.value:
            if current.left is None:
                current.left = Node(value)
            else:
                self._insert_recursive(current.left, value)
        # se o valor for maior, o nó será inserido na subárvore direita
        elif value > current.value:
            if current.right is None:
                current.right = Node(value)
            else:
                self._insert_recursive(current.right, value)

    # percorre a árvore em pré-ordem
    def preorder(self):
        result = []
        self._preorder_recursive(self.root, result)
        return result

    # funç recursiva para percurso pré-ordem
    def _preorder_recursive(self, node, result):
        if node:
            result.append(node.value)  # visita o nó raiz
            self._preorder_recursive(node.left, result)  # percorre à esquerda
            self._preorder_recursive(node.right, result)  # percorre à direita

    # percorre a árvore em em-ordem
    def inorder(self):
        result = []
        self._inorder_recursive(self.root, result)
        return result

    # funç recursiva para percurso em ordem
    def _inorder_recursive(self, node, result):
        if node:
            self._inorder_recursive(node.left, result)  # percorre à esquerda
            result.append(node.value)  # visita o nó raiz
            self._inorder_recursive(node.right, result)  # percorre à direita

    # percorre a árvore em pós-ordem
    def postorder(self):
        result = []
        self._postorder_recursive(self.root, result)
        return result

    # funç recursiva para percurso pós-ordem
    def _postorder_recursive(self, node, result):
        if node:
            self._postorder_recursive(node.left, result)  # percorre à esquerda
            self._postorder_recursive(node.right, result)  # percorre à direita
            result.append(node.value)  # visita o nó raiz

    # calcula a altura da árvore
    def height(self):
        return self._height_recursive(self.root)

    # funç recursiva para calcular a altura
    def _height_recursive(self, node):
        if node is None:
            return 0
        else:
            left_height = self._height_recursive(node.left)
            right_height = self._height_recursive(node.right)
            return max(left_height, right_height) + 1

    # busca um valor na árvore binária de busca
    def search(self, value):
        return self._search_recursive(self.root, value)

    # funç recursiva para buscar um valor
    def _search_recursive(self, node, value):
        if node is None:
            return None
        if value == node.value:
            return node
        elif value < node.value:
            return self._search_recursive(node.left, value)
        else:
            return self._search_recursive(node.right, value)

# inserção paralela em subárvores esquerda e direita
def parallel_insert(tree, value):
    if tree.root is None:
        tree.root = Node(value)
    else:
        # criando threads para inserir nas subárvores esquerda e direita
        left_thread = threading.Thread(target=insert_subtree, args=(tree.root.left, value))
        right_thread = threading.Thread(target=insert_subtree, args=(tree.root.right, value))
        left_thread.start()
        right_thread.start()
        left_thread.join()
        right_thread.join()

# funç auxiliar para inserir em subárvores específicas
def insert_subtree(node, value):
    if value < node.value:
        if node.left is None:
            node.left = Node(value)
        else:
            insert_subtree(node.left, value)
    elif value > node.value:
        if node.right is None:
            node.right = Node(value)
        else:
            insert_subtree(node.right, value)

tree = BinaryTree()
tree.insert(10)
tree.insert(20)
tree.insert(5)

# verificando percursos:
print("Pré-ordem:", tree.preorder())
print("Em-ordem:", tree.inorder())
print("Pós-ordem:", tree.postorder())

# altura da árvore:
print("Altura:", tree.height())

# buscando um valor:
print("Buscando 10:", tree.search(10) is not None)
