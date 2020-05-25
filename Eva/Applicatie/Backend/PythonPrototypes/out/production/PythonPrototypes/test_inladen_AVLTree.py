from unittest import TestCase

from AVLtree import AVLTree
from VariableNode import VariableNode


class Test_AVLTree(TestCase):

    def test_add_left_child(self):
        keys = [3, 2]
        avl_tree = self.create_tree(keys, 3)

        self.assert_node_has_one_left_child(avl_tree.root)

    def test_add_right_child(self):
        keys = [2, 3]
        avl_tree = self.create_tree(keys, 2)

        self.assert_node_has_one_right_child(avl_tree.root)

    def test_add_two_right_childs(self):
        keys = [2, 3, 4]
        avl_tree = self.create_tree(keys, 2)

        self.assert_node_has_two_children(avl_tree.root)

    def test_add_four_right_children(self):
        keys = [2,3,4,5,6]
        initNumber = 2
        avl_tree = self.create_tree(keys, initNumber)

        self.assert_node_has_two_children(avl_tree.root)
        self.assert_node_has_two_children(avl_tree.root.right)

    def test_find(self):
        keys = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        avl_tree = self.create_tree(keys, 10)

        for key in keys:
            result = avl_tree.find(key)
            self.assert_found(key, result)


    def create_tree(self, keys, initial_number):
        avl_tree = AVLTree()
        avl_tree.root = avl_tree.insert(None, initial_number, initial_number)
        for key in keys:
            if key == initial_number:
                continue
            tmp = avl_tree.insert(avl_tree.root, key, key)
            avl_tree.root = tmp
        return avl_tree

    def assert_found(self, key2, result):
        self.assertEqual(key2, result.key)

    def create_node(self, key, value):
        variable = VariableNode(key)
        variable.value = value
        return variable

    def assert_root_has_correct_key_and_value(self, node, variable):
        self.assertEqual(variable.value, node.value)
        self.assertEqual(variable.key, node.key)

    def assert_node_has_one_right_child(self, node):
        self.assertEqual(None, node.left)
        self.assertEqual(type(VariableNode("a")), node.right.__class__)

    def assert_node_has_one_left_child(self, node):
        self.assertEqual(type(VariableNode("a")), node.left.__class__)
        self.assertEqual(None, node.right)

    def assert_node_has_no_children(self, node):
        self.assertEqual(None, node.left)
        self.assertEqual(None, node.right)

    def test_right_rotate(self):
        expected = self.create_node(10, 2)
        expected.right = self.create_node(12, 2)
        expected.left = self.create_node(9, 2)
        expected.right.left = self.create_node(11, 2)
        expected.right.right = self.create_node(13, 2)

        root = self.create_node(12, 2)
        root.left = self.create_node(10, 2)
        root.left.left = self.create_node(9, 2)
        root.left.right = self.create_node(11, 2)
        root.right = self.create_node(13, 2)

        avl_tree = AVLTree()
        k2 = avl_tree.right_rotate(root)

        resultValues = self.get_values_in_order(k2)
        expectedValues = self.get_values_in_order(expected)

        self.assertEqual(resultValues, expectedValues)

    def test_left_rotate(self):
        expected = self.create_node(12, 2)
        expected.left = self.create_node(10, 1)
        expected.left.left = self.create_node(9, 2)
        expected.left.right = self.create_node(11, 2)
        expected.right = self.create_node(13, 2)
        expectedValues = self.get_values_in_order(expected)
        root = self.create_node(10, 1)
        root.right = self.create_node(12, 2)
        root.right.left = self.create_node(11, 2)
        root.right.right = self.create_node(13, 2)
        root.left = self.create_node(9, 2)
        avl_tree = AVLTree()

        k2 = avl_tree.left_rotate(root)

        resultValues = self.get_values_in_order(k2)

        self.assertEqual(resultValues, expectedValues)

    def test_get_height(self):
        keys = [9, 10, 8]
        expectedResult = 2
        avl_tree = self.create_tree(keys, 9)

        result = avl_tree.get_height(avl_tree.root)
        self.assertEqual(expectedResult, result)

    def get_values_in_order(self, root):
        values =[]
        self.__get_values_in_order(root, values)
        return values

    def __get_values_in_order(self, root, list):
        if root.left is not None:
            self.__get_values_in_order(root.left, list)
        list.append(root.key)
        if root.right is not None:
            self.__get_values_in_order(root.right, list)

    def assert_node_has_two_children(self, root):
        self.assertEqual(type(VariableNode("a")), root.left.__class__)
        self.assertEqual(type(VariableNode("a")), root.right.__class__)

    def runTest(self):
        self.test_add_left_child()
        self.test_add_right_child()
        self.test_find()
        self.test_add_four_right_children()
        self.test_add_two_right_childs()
        self.test_get_height()
        self.test_left_rotate()
        self.test_right_rotate()


