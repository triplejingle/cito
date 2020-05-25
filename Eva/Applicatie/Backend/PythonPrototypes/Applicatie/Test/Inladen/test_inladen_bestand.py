import unittest

from Tool.Test.Excel_Library import Excel
from File import File
from Reader import ExcelReader


class Test_Bestand(unittest.TestCase):
    path = "./sources/"
    bestand = File()
    reader = ExcelReader()
    def test_readExcelBestandWithContent(self):
        ExcelTestSuite = Excel()
        file = "test_readExcelbestandWithContent.xlsx"
        data = [
            ["Plaats", "School", "Niveau", "Leerling", "Score", "Label"],
            ["Apeldoorn", "HAN", "HBO", "563631", "15", "test1"]
        ]
        ExcelTestSuite.create_document(self.path + file)
        ExcelTestSuite.add_worksheet()
        ExcelTestSuite.add_data_to_document(data)
        ExcelTestSuite.save_document()

        self.assertDocumentHasContent(data, self.path + file)

        ExcelTestSuite.remove_document(self.path + file)

    def test_load_niveaus(self):
        excel_test_suite = Excel()
        file = "test_loadNiveaus.xlsx"
        data = [
            ["Plaats", "School", "Niveau", "Leerling", "Score", "Label"],
            ["Apeldoorn", "HAN", "HBO", "563631", "15", "test1"]
        ]
        excel_test_suite.create_document(self.path + file)
        excel_test_suite.add_worksheet()
        excel_test_suite.add_data_to_document(data)
        excel_test_suite.save_document()

        content = self.reader.read_content(self.path + file)
        self.assertDocumentHasNiveaus(data, content)

        excel_test_suite.remove_document(self.path + file)

    def test_readEmptyExcelbestand(self):
        excel_test_suite = Excel()
        file = "test_readEmptyExcelbestand.xlsx"
        self.createEmptyExcelBestand(self.path + file)

        content = self.reader.read_content(self.path + file)

        self.assertDocumentHasNoContent(content)

        excel_test_suite.remove_document(self.path + file)


    def assertDocumentHasNiveaus(self, data, content):
        self.assertEqual(data[0], self.bestand.load_levels(content))

    def createEmptyExcelBestand(self, file):
        ExcelTestSuite = Excel()
        ExcelTestSuite.create_document(file)
        ExcelTestSuite.add_worksheet()
        ExcelTestSuite.save_document()

    def assertDocumentHasNoContent(self, content):
        self.assertEqual(0, len(content))

    def assertDocumentContains(self, value, row, column, file_name):
        self.assertEqual(value, self.bestand.readCellData(row, column, file_name))

    def assertDocumentHasContent(self, data, file_name):
        self.assertEqual(data, self.reader.read_content(file_name))

    def runTest(self):
        self.test_load_niveaus()
        self.test_readEmptyExcelbestand()
        self.test_readExcelBestandWithContent()

if __name__ == '__main__':
    unittest.main()
