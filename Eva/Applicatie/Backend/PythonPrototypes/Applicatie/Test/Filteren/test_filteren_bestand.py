from unittest import TestCase

from File import File
from Level import Level
from Tool.Test.Excel_Library import Excel


class Test_Bestand(TestCase):
    path = "./sources/"
    def test_get_filter_criteria(self):
        bestand = File()
        excel_test_suite = Excel()
        file = "test_get_filter_criteria.xlsx"
        data = [
            ["Plaats", "School", "Niveau", "Leerling", "Score", "Label"],
            ["Apeldoorn", "HAN", "HBO", "563631", "15", "test1"]
        ]
        excel_test_suite.create_document(self.path + file)
        excel_test_suite.add_worksheet()
        excel_test_suite.add_data_to_document(data)
        excel_test_suite.save_document()

        bestand.load(self.path + file)

        excel_test_suite.remove_document(self.path + file)


    def test_get_levels(self):
        incoming_criteria = [{ "name":"Label","variables":[]},{"name":"Leerling","variables":[]},
                             {"name":"Niveau","variables":[]},{"name":"Plaats","variables":[]},
                             {"name":"School","variables":[]},{"name":"Score","variables":[]}]

        file = File()
        expected = ["Label", "Leerling", "Niveau", "Plaats", "School", "Score"]
        data = [
            ["Label", "Leerling", "Niveau", "Plaats", "School", "Score"],
            ["test1", "563631", "HBO", "Apeldoorn", "HAN", "15"]
        ]

        self.create_levels(file, expected, data)
        result = file.get_levels(incoming_criteria)

        for x in range(0, len(expected)):
            self.assertEqual(expected[x], result[x].name)

    def test_get_variables(self):
        incoming_criteria = [{"name": "Plaats","variables": ["Apeldoorn","Arnhem"]}]
        bestand = File()
        expected = ['Apeldoorn', 'Arnhem']

        result = bestand.get_variables('Plaats', incoming_criteria)

        self.assertEquals(expected, result)

    def test_remove_duplicate_indexes(self):
        indexes = [2, 3, 4, 5, 6, 0, 2, 3, 4, 6]
        expected = [0, 2, 3, 4, 5, 6]
        bestand = File()
        bestand.filtered_list = indexes

        bestand.remove_duplicate_row_numbers()

        result = bestand.filtered_list

        self.assertEqual(expected, result)

    def test_remove_single_indexes(self):
        indexes = [2, 2, 2, 4, 4, 4, 0]
        expected = [2, 4]
        bestand = File()
        bestand.filtered_list = indexes

        bestand.remove_single_row_numbers(3)

        result = bestand.filtered_list

        self.assertEqual(expected, result)

    def create_levels(self, bestand, expected, content):
        for name in expected:
            niveau = Level()
            niveau.create_level(content, name)
            bestand.levels.append(niveau)

    def runTest(self):
        self.test_get_filter_criteria()
        self.test_get_levels()
        self.test_get_variables()
        self.test_remove_duplicate_indexes()
        self.test_remove_single_indexes()
