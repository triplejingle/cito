from unittest import TestCase

from BinarySearchTree import BinarySearchTree
from Niveau import Niveau


class Test_niveau(TestCase):
    def test_create_niveau(self):
        content = [["Plaats", "School", "Niveau", "Leerling", "Score", "Label"],
                   ["Apeldoorn", "HAN", "HBO", "563631", "15", "test1"],
                   ["Arnhem", "HAN", "HBO", "563631", "15", "test1"]]
        niveau = Niveau()
        binary_search_tree = BinarySearchTree()
        binary_search_tree.insert(content[1][0], 0)
        binary_search_tree.insert(content[2][0], 1)
        expected_niveau = "Plaats"

        niveau.create_niveau(content, content[0][0])

        self.assertEqual(expected_niveau, niveau.name)
        self.assertEqual(binary_search_tree.find('Apeldoorn').key, niveau.variabelen.find('Apeldoorn').key)
        self.assertEqual(binary_search_tree.find('Arnhem').key, niveau.variabelen.find('Arnhem').key)

    def test_get_variables(self):
        content = [["Plaats", "School", "Niveau", "Leerling", "Score", "Label"],
                   ["Apeldoorn", "HAN", "HBO", "563631", "15", "test1"],
                   ["Arnhem", "HAN", "HBO", "563631", "15", "test1"]]
        niveau = Niveau()
        expected_result = ["Apeldoorn", "Arnhem"]
        column_number = 0
        niveau.name = "Plaats"

        variables = niveau.get_variables(column_number, content)

        self.assert_get_variables_contains(expected_result, variables)

    def test_get_column_index(self):
        content = [
            ["Plaats", "School", "Niveau", "Leerling", "Score", "Label"],
            ["Apeldoorn", "HAN", "HBO", "563631", "15", "test1"]]
        niveau = Niveau()
        niveau.name = "School"
        column_number = 1

        result = niveau.get_column_index(content)

        self.assert_niveau_is_in_column_number(column_number, result)

    def assert_get_variables_contains(self, expected_result, variables):
        self.assertEqual(expected_result, variables)

    def assert_niveau_is_in_column_number(self, column_number, result):
        self.assertEqual(column_number, result)

    def runTest(self):
        self.test_create_niveau()
        self.test_get_column_index()
        self.test_get_variables()
