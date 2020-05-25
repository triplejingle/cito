from unittest import TestCase

from BinarySearchTree import BinarySearchTree
from VariableNode import VariableNode


class TestBinarySearchTree(TestCase):

    def test_add_one_number(self):
        key = "Apeldoorn"
        value = 1
        variable = self.create_node(key, value)
        binary_search_tree = BinarySearchTree()

        binary_search_tree.insert(key, value)

        self.assert_root_has_correct_key_and_value(binary_search_tree.root, variable)
        self.assert_node_has_no_children(binary_search_tree.root)

    def test_add_left_child(self):
        key1 = 2
        key2 = 1
        key3 = 0
        value1 = 1
        value2 = 2
        binary_search_tree = BinarySearchTree()

        binary_search_tree.insert(key1, value2)
        binary_search_tree.insert(key2, value1)
        binary_search_tree.insert(key3, value1)

        self.assert_node_has_one_left_child(binary_search_tree.root)
        self.assert_node_has_one_left_child(binary_search_tree.root.left)

    def test_add_right_child(self):
        key1 = 1
        key2 = 2
        value1 = 1
        value2 = 2
        binary_search_tree = BinarySearchTree()

        binary_search_tree.insert(key1, value1)
        binary_search_tree.insert(key2, value2)

        self.assert_node_has_one_right_child(binary_search_tree.root)

    def test_find_leaf(self):
        keys = {1, 2, 3}
        binary_search_tree = BinarySearchTree()
        for key in keys:
            binary_search_tree.insert(key, key)

        result = binary_search_tree.find_leaf(binary_search_tree.root)

        self.assert_node_has_no_children(result)

    def test_find(self):
        key1 = 2
        key2 = 1
        key3 = 0
        value1 = 1
        value2 = 2
        binary_search_tree = BinarySearchTree()
        binary_search_tree.insert(key1, value2)
        binary_search_tree.insert(key2, value1)
        binary_search_tree.insert(key3, value1)

        result = binary_search_tree.find(key2)

        self.assert_found(key2, result)

    def test_find(self):
        key1 = 2
        key2 = 1
        key3 = 0
        value1 = 1
        value2 = 2
        binary_search_tree = BinarySearchTree()
        binary_search_tree.insert(key1, value2)
        binary_search_tree.insert(key2, value1)
        binary_search_tree.insert(key3, value1)

        result = binary_search_tree.find(key3)

        self.assert_found(key3, result)

    def test_find(self):
        key1 = 2
        key2 = 1
        key3 = 0
        value1 = 1
        value2 = 2
        binary_search_tree = BinarySearchTree()
        binary_search_tree.insert(key1, value2)
        binary_search_tree.insert(key2, value1)
        binary_search_tree.insert(key3, value1)

        result = binary_search_tree.find(key1)

        self.assert_found(key1, result)

    def assert_found(self, key2, result):
        self.assertEqual(key2, result.key)

    def test_find_min(self):
        key1 = 2
        key2 = 1
        key3 = 0
        value1 = 1
        value2 = 2
        binary_search_tree = BinarySearchTree()
        binary_search_tree.insert(key1, value2)
        binary_search_tree.insert(key2, value1)
        binary_search_tree.insert(key3, value1)
        lowest_key = key3
        result = binary_search_tree.find_min()

        self.assert_lowest_found(lowest_key, result)

    def assert_lowest_found(self, lowest_key, result):
        self.assertEqual(lowest_key, result.key)

    def test_findMax(self):
        key1 = 2
        key2 = 1
        key3 = 0
        value1 = 1
        value2 = 2
        binary_search_tree = BinarySearchTree()
        binary_search_tree.insert(key1, value2)
        binary_search_tree.insert(key2, value1)
        binary_search_tree.insert(key3, value1)
        highest_key = key1

        result = binary_search_tree.find_max()

        self.assertHighestFound(highest_key, result)

    def assertHighestFound(self, highest_key, result):
        self.assertEqual(highest_key, result.key)

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

    def runTest(self):
        self.test_add_left_child()
        self.test_add_one_number()
        self.test_add_right_child()
        self.test_find()
        self.test_find_leaf()
        self.test_find_min()
        self.test_findMax()
