class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:

    def __init__(self):
        self.root = None
        self.keys = []
        self.size = 0

    #A implementar: verificador de chave repetida. Se a chave já existir, não insere e retorna False
    def insert(self, key):
        if key in self.keys:
            return False
        self.root = self._insert_recursively(self.root, key)
        self.keys.append(key)
        self.size += 1

    def _insert_recursively(self, root, key):
        if root is None:
            return Node(key)
        if key < root.key:
            root.left = self._insert_recursively(root.left, key)
        elif key > root.key:
            root.right = self._insert_recursively(root.right, key)
        return root

    #listar todas as chaves da árvore em ordem crescente
    def list(self):
        return self._list_recursively(self.root)

    def _list_recursively(self, root):
        if root is not None:
            self._list_recursively(root.left)
            self.nodes.append(root.key)
            self._list_recursively(root.right)
        return self.keys

    def search(self, key):
        return self._search_recursively(self.root, key)

    def _search_recursively(self, root, key):
        if root is None or root.key == key:
            return root
        if key < root.key:
            return self._search_recursively(root.left, key)
        return self._search_recursively(root.right, key)

    def inorder_traversal(self):
        result = []
        self._inorder_traversal_recursively(self.root, result)
        return result

    def _inorder_traversal_recursively(self, root, result):
        if root is not None:
            self._inorder_traversal_recursively(root.left, result)
            result.append(root.key)
            self._inorder_traversal_recursively(root.right, result)

    def preorder_traversal(self):
        result = []
        self._preorder_traversal_recursively(self.root, result)
        return result

    def _preorder_traversal_recursively(self, root, result):
        if root is not None:
            result.append(root.key)
            self._preorder_traversal_recursively(root.left, result)
            self._preorder_traversal_recursively(root.right, result)

    def postorder_traversal(self):
        result = []
        self._postorder_traversal_recursively(self.root, result)
        return result

    def _postorder_traversal_recursively(self, root, result):
        if root is not None:
            self._postorder_traversal_recursively(root.left, result)
            self._postorder_traversal_recursively(root.right, result)
            result.append(root.key)

    def find_min(self):
        return self._find_min_recursively(self.root)

    def _find_min_recursively(self, root):
        if root.left is None:
            return root.key
        return self._find_min_recursively(root.left)

    def find_max(self):
        return self._find_max_recursively(self.root)

    def _find_max_recursively(self, root):
        if root.right is None:
            return root.key
        return self._find_max_recursively(root.right)

    def get_height(self, node):
        if node is None:
            return 0
        return 1 + max(self.get_height(node.left), self.get_height(node.right))

        

    '''#arrumar - não está funcionando corretamente
    def is_balanced(self):
        if self.root is None:
            return True
        return abs(self.get_height(self.root.left) - self.get_height(self.root.right)) <= 1 and \
            self.is_balanced(self.root.left) and \
            self.is_balanced(self.root.right)
    
    def _is_balanced_recursively(self, root):
        if root is None:
            return'''

    def get_size(self):
        """Retorna o número de elementos na árvore."""
        if self.root is None:
            return 0
        return self._get_size(self.root)

    def _get_size(self, node):
        if node is None:
            return 0
        return 1 + self._get_size(node.left) + self._get_size(node.right)
    
    def get_inner_length(self, node):
        """Retorna o número de elementos na árvore, excluindo a raíz."""
        if node is None:
            return 0
        return self.get_inner_length(node.left) + self.get_inner_length(node.right) + 1

    
    def is_balanced(self):
        """Verifica se a árvore é balanceada."""
        if self.root is None:
            return True
        return self._is_balanced_recursively(self.root)

    def _is_balanced_recursively(self, node):
        if node is None or node.left is None and node.right is None:
            return True

        left_height = self.get_height(node.left)
        right_height = self.get_height(node.right)

        return abs(left_height - right_height) <= 1 and \
            self._is_balanced_recursively(node.left) and \
            self._is_balanced_recursively(node.right)



    def get_traversal(self, traversal_type):
        """Retorna uma lista com os elementos da árvore, ordenados de acordo com o tipo de travessia especificado."""
        if traversal_type == "inorder":
            return self.inorder_traversal()
        elif traversal_type == "preorder":
            return self.preorder_traversal()
        elif traversal_type == "postorder":
            return self.postorder_traversal()
        else:
            raise ValueError("Tipo de travessia inválido.")


