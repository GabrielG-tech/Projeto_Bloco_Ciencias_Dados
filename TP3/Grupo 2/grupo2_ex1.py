import threading

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    # insere um nó na árvore binária de forma paralela
    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    # função recursiva que insere um nó na árvore
    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                left_thread = threading.Thread(target=self._insert_recursive, args=(node.left, value))
                left_thread.start()
                left_thread.join()
        elif value > node.value:
            if node.right is None:
                node.right = Node(value)
            else:
                right_thread = threading.Thread(target=self._insert_recursive, args=(node.right, value))
                right_thread.start()
                right_thread.join()

    # percorre a árvore em pré-ordem (root-left-right) com computação paralela
    def preorder(self):
        result = []
        self._preorder_recursive(self.root, result)
        return result

    def _preorder_recursive(self, node, result):
        if node:
            result.append(node.value)
            threads = []
            if node.left:
                left_thread = threading.Thread(target=self._preorder_recursive, args=(node.left, result))
                threads.append(left_thread)
                left_thread.start()
            if node.right:
                right_thread = threading.Thread(target=self._preorder_recursive, args=(node.right, result))
                threads.append(right_thread)
                right_thread.start()

            for thread in threads:
                thread.join()

    # percorre a árvore em em-ordem (left-root-right) com computação paralela
    def inorder(self):
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, node, result):
        if node:
            threads = []
            if node.left:
                left_thread = threading.Thread(target=self._inorder_recursive, args=(node.left, result))
                threads.append(left_thread)
                left_thread.start()

            for thread in threads:
                thread.join()

            result.append(node.value)

            if node.right:
                right_thread = threading.Thread(target=self._inorder_recursive, args=(node.right, result))
                right_thread.start()
                right_thread.join()

    # percorre a árvore em pós-ordem (left-right-root) com computação paralela
    def postorder(self):
        result = []
        self._postorder_recursive(self.root, result)
        return result

    def _postorder_recursive(self, node, result):
        if node:
            threads = []
            if node.left:
                left_thread = threading.Thread(target=self._postorder_recursive, args=(node.left, result))
                threads.append(left_thread)
                left_thread.start()
            if node.right:
                right_thread = threading.Thread(target=self._postorder_recursive, args=(node.right, result))
                threads.append(right_thread)
                right_thread.start()

            for thread in threads:
                thread.join()

            result.append(node.value)

    # buscar um valor na árvore binária de busca com computação paralela
    def search(self, value):
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        if node is None:
            return None
        if node.value == value:
            return node

        threads = []
        results = [None]

        if node.left:
            left_thread = threading.Thread(target=self._search_worker, args=(node.left, value, results))
            threads.append(left_thread)
            left_thread.start()

        if node.right:
            right_thread = threading.Thread(target=self._search_worker, args=(node.right, value, results))
            threads.append(right_thread)
            right_thread.start()

        for thread in threads:
            thread.join()

        return results[0]

    def _search_worker(self, node, value, results):
        if results[0] is None:  # evita sobrescrever resultado
            found = self._search_recursive(node, value)
            if found:
                results[0] = found

tree = BinaryTree()
tree.insert(10)
tree.insert(20)
tree.insert(5)

print("Pré-ordem:", tree.preorder())
print("Em-ordem:", tree.inorder())
print("Pós-ordem:", tree.postorder())
print("Buscando 10:", tree.search(10) is not None)
