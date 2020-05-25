from VariableNode import VariableNode


class BinarySearchTree(object):
    def __init__(self):
        self.root = None

    def find(self, key):
        if self.root.key == key:
            return self.root
        if self.root.key < key:
            return self.__find(self.root.right, key)
        if self.root.key > key:
            return self.__find(self.root.left, key)

    def __find(self, node, key):
        if node.key < key:
            node = self.__find(node.right, key)
        if node.key > key:
            node = self.__find(node.left, key)
        return node

    def insert(self, key, value):
        node = VariableNode(key)
        node.value = value
        if self.root is None:
            self.root = node
            return
        self.__insert(self.root, key, value)

    def __insert(self, root, key, value):
        node = VariableNode(key)
        node.value = value
        if root.key < key:
            if root.right is None:
                root.right = node
                return
            self.__insert(root.right, key, value)
        if root.key > key:
            if root.left is None:
                root.left = node
                return
            self.__insert(root.left, key, value)

    def find_leaf(self, root):
        if root.left is not None:
            return self.find_leaf(root.left)
        if root.right is not None:
            return self.find_leaf(root.right)
        return root

    def find_min(self):
        return self.__find_min(self.root)

    def __find_min(self, node):
        if node.left is not None:
            return self.__find_min(node.left)
        return node

    def find_max(self):
        return self.__find_max(self.root)

    def __find_max(self, node):
        if node.right is not None:
            return self.__find_max(node.right)
        return node
