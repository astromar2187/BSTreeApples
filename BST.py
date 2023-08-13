class Node:
        def __init__(self, key):
            self.key = key
            self.left = None
            self.right = None

class BST:

    def __init__(self):
        self.root = None
        self.keys = []

    #A implementar: verificador de chave repetida. Se a chave já existir, não insere e retorna False
    def insert(self, key):
        self.root = self._insert_recursively(self.root, key)
        self.keys.append(key)

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
        return self._find_max_rec
    
    #arrumar - não está funcionando corretamente
    def is_balanced(self):
        return self._is_balanced_recursively(self.root)

    def _is_balanced_recursively(self, root):
        if root is None:
            return True

        left_height = self._get_height(root.left)
        right_height = self._get_height(root.right)

        if abs(left_height - right_height) > 1:
            return False

        return (self._is_balanced_recursively(root.left) and
                self._is_balanced_recursively(root.right))

    def _get_height(self, node):
        if node is None:
            return 0

        left_height = self._get_height(node.left)
        right_height = self._get_height(node.right)

        return max(left_height, right_height) + 1
