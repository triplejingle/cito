from VariableNode import VariableNode


class AVLTree(object):
    root = None

    def insert(self, root, key, value):
        node = VariableNode(key)
        node.value.append(value)
        if root is None:
            return node
        if key < root.key:
            root.left = self.insert(root.left, key, value)
        if key > root.key:
            root.right = self.insert(root.right, key, value)
        if key == root.key:
            root.value.append(value)
            return root
        root.height = 1 + max(self.get_height(root.left),self.get_height(root.right))
        balance = self.get_balance(root)
        root = self.rebalance(balance, key, root)
        return root

    def rebalance(self, balance, key, root):
        # Step 4 - If the node is unbalanced,
        # then try out the 4 cases
        # Case 1 - Left Left
        if balance > 1 and key < root.left.key:
            root = self.right_rotate(root)
        # Case 3 - Left Right
        if balance > 1 and key > root.left.key:
            root.left = self.left_rotate(root.left)
            root = self.right_rotate(root)
        # Case 2 - Right Right
        if balance < -1 and key > root.right.key:
            root = self.left_rotate(root)
        # Case 4 - Right Left
        if balance < -1 and key < root.right.key:
            root.right = self.right_rotate(root.right)
            root = self.left_rotate(root)
        return root

    @staticmethod
    def is_right_side_unbalanced(balance):
        right_part_is_unbalanced = -1
        return balance < right_part_is_unbalanced

    @staticmethod
    def is_left_side_unbalanced(balance):
        left_part_is_unbalanced = 1
        return balance > left_part_is_unbalanced

    @staticmethod
    def left_rotate(k1):
        k2 = k1.right
        b = k2.left

        k2.left = k1
        k1.right = b
        return k2

    @staticmethod
    def right_rotate(k2):
        k1 = k2.left
        b = k1.right

        k1.right = k2
        k2.left = b

        return k1

    @staticmethod
    def get_height(node):
        if not node:
            return 0

        return node.height

    def get_balance(self, node):
        if not node:
            return 0

        return self.get_height(node.left) - self.get_height(node.right)

    def find(self, key):
        if self.root.key == key:
            return self.root
        if self.root.key < key:
            return self.__find(self.root.right, key)
        if self.root.key > key:
            return self.__find(self.root.left, key)

    def __find(self, node, key):
        result = node
        if node.key < key:
            result = self.__find(node.right, key)
        if node.key > key:
            result = self.__find(node.left, key)
        return result
