class TrieNode:
    def __init__(self):
        # cada nó possui um dicionário de filhos e um indicador de fim de palavra
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        # inicializa a Trie com um nó raiz vazio
        self.root = TrieNode()

    def inserir(self, palavra):
        # insere uma palavra na trie
        node = self.root
        for char in palavra:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def buscar(self, palavra):
        # busca uma palavra na trie e retorna True se encontrada, False caso contrário
        node = self.root
        for char in palavra:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def deletar(self, palavra):
        # deleta uma palavra da trie
        def deletar_recursivo(node, palavra, index):
            if index == len(palavra):
                if not node.is_end_of_word:
                    return False
                node.is_end_of_word = False
                return len(node.children) == 0
            char = palavra[index]
            if char not in node.children:
                return False
            can_delete_node = deletar_recursivo(node.children[char], palavra, index + 1)
            if can_delete_node:
                del node.children[char]
                return len(node.children) == 0
            return False
        
        deletar_recursivo(self.root, palavra, 0)

    def autocomplete(self, prefixo):
        # retorna uma lista de palavras que começam com o prefixo
        node = self.root
        for char in prefixo:
            if char not in node.children:
                return []
            node = node.children[char]
        palavras = []
        self._autocomplete_recursivo(node, prefixo, palavras)
        return palavras

    def _autocomplete_recursivo(self, node, prefixo, palavras):
        if node.is_end_of_word:
            palavras.append(prefixo)
        for char, child_node in node.children.items():
            self._autocomplete_recursivo(child_node, prefixo + char, palavras)

    def contar_prefixos(self, prefixo):
        # conta quantas palavras na trie começam com o prefixo
        node = self.root
        for char in prefixo:
            if char not in node.children:
                return 0
            node = node.children[char]
        return self._contar_prefixos_recursivo(node)

    def _contar_prefixos_recursivo(self, node):
        count = 1 if node.is_end_of_word else 0
        for child_node in node.children.values():
            count += self._contar_prefixos_recursivo(child_node)
        return count

trie = Trie()

palavras = ["gato", "galo", "gafanhoto", "golfinho", "girafa"]
for palavra in palavras:
    trie.inserir(palavra)

print("Buscar 'gato':", trie.buscar("gato"))  # True
print("Buscar 'galo':", trie.buscar("galo"))  # True
print("Buscar 'gaviao':", trie.buscar("gaviao"))  # False

print("Autocomplete de 'ga':", trie.autocomplete("ga"))  # ['gato', 'galo', 'gafanhoto', 'golfinho']
print("Autocomplete de 'gi':", trie.autocomplete("gi"))  # ['girafa']

print("Contar prefixos 'ga':", trie.contar_prefixos("ga"))  # 4 (gato, galo, gafanhoto, golfinho)

trie.deletar("galo")
print("Buscar 'galo' após deletar:", trie.buscar("galo"))  # False
