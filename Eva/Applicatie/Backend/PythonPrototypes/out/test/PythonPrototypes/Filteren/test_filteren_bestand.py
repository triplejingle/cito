from unittest import TestCase

from Bestand import Bestand
from Niveau import Niveau


class Test_Bestand(TestCase):

    def test_getFilterCriteria(self):
        bestand = Bestand()
        criteria = bestand.get_filter_criteria()

    def test_getNiveaus(self):
        incoming_criteria = ["Label", "Leerling", "Niveau", "Plaats", "School", "Score"]

        bestand = Bestand()
        expected = ["Label", "Leerling", "Niveau", "Plaats", "School", "Score"]
        data = [
            ["Label", "Leerling", "Niveau", "Plaats", "School", "Score"],
            ["test1", "563631", "HBO", "Apeldoorn", "HAN", "15"]
        ]
        self.createNiveaus(bestand, expected, data)
        result = bestand.get_niveaus(incoming_criteria)

        for x in range(0, len(expected)):
            self.assertEqual(expected[x], result[x].name)

    def test_getVariables(self):
        incoming_criteria = {"Plaats": ["Apeldoorn","Arnhem"]}
        bestand = Bestand()
        expected = ['Apeldoorn', 'Arnhem']

        result = bestand.get_variables('Plaats', incoming_criteria)

        self.assertEquals(expected, result)

    def test_removeDuplicateIndexes(self):
        indexes = [2, 3, 4, 5, 6, 0, 2, 3, 4, 6]
        expected = [0, 2, 3, 4, 5, 6]
        bestand = Bestand()
        bestand.index_list = indexes

        bestand.remove_duplicate_indexes()

        result = bestand.index_list

        self.assertEqual(expected, result)

    def test_removeSingleIndexes(self):
        indexes = [2, 2, 2, 4, 4, 4, 0]
        expected = [2, 4]
        bestand = Bestand()
        bestand.index_list = indexes

        bestand.remove_single_indexes(3)

        result = bestand.index_list

        self.assertEqual(expected, result)

    def createNiveaus(self, bestand, expected, content):
        for name in expected:
            niveau = Niveau()
            niveau.create_niveau(content, name)
            bestand.niveaus.append(niveau)
    def runTest(self):
        self.test_getFilterCriteria()
        self.test_getNiveaus()
        self.test_getVariables()
        self.test_removeDuplicateIndexes()
        self.test_removeSingleIndexes()
