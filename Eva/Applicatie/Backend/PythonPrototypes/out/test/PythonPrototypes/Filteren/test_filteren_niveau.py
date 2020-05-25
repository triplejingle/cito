from unittest import TestCase

from AVLtree import AVLTree
from Niveau import Niveau


class Test_niveau(TestCase):
    def test_get_filter_criteria(self):
        content = [["Plaats", "School", "Niveau", "Leerling", "Score", "Label"],
                   ["Apeldoorn", "HAN", "HBO", "563631", "15", "test1"],
                   ["Arnhem", "HAN", "HBO", "563631", "15", "test1"]]
        expected_column = [["Apeldoorn", "Arnhem"], ["HAN"], ["HBO"], ["563631"], ["15"], ["test1"]]
        niveau = Niveau()
        for x in range(0, len(content[0])):
            column_number = x
            niveau.name = content[0][column_number]
            niveau.set_filter_criteria(column_number, content)
            self.assertEqual(expected_column[column_number], niveau.filtered_criteria)
            niveau.filtered_criteria = []

    def test_search(self):
        niveau = Niveau()
        avl_tree = AVLTree()
        root = avl_tree.insert(None, 'Apeldoorn', 0)
        new_root = avl_tree.insert(root, 'Arnhem', 1)
        avl_tree.root = new_root
        niveau.variabelen = avl_tree
        expected = [1]
        variables = 'Arnhem'

        result = niveau.search(variables)

        self.assertEqual(expected, result)

    def test_add_indexes_to_filtered_list(self):
        indexes_part_one = [0, 1, 2, 3, 4, 5, 6]
        indexes_part_two = [0, 1, 2, 3, 4, 5, 6]
        expected = [0, 1, 2, 3, 4, 5, 6, 0, 1, 2, 3, 4, 5, 6]
        niveau = Niveau()

        niveau.add_indexes_to_filtered_list(indexes_part_one)
        niveau.add_indexes_to_filtered_list(indexes_part_two)

        result = niveau.indexes

        self.assertEqual(expected, result)
    def runTest(self):
        self.test_add_indexes_to_filtered_list()
        self.test_get_filter_criteria()
        self.test_search()
