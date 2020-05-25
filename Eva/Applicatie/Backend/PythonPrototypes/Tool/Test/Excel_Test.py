import unittest

from Tool.Test.Excel_Library import Excel


class ExcelTest(unittest.TestCase):
    testExcelSuite = Excel()
    basePath = "./sources/"
    def test_add_data(self):
        data = [
            ["Plaats", "School", "Niveau", "Leerling", "Score", "Label"],
            ["Apeldoorn", "HAN", "HBO", "563631", "15", "test1"]
        ]
        file_name = "testAddDataToDocument.xlsx"
        self.testExcelSuite.create_document(self.basePath + file_name)
        self.testExcelSuite.add_worksheet()

        self.testExcelSuite.add_data_to_document(data)
        self.testExcelSuite.save_document()

        self.assert_document_contains_data(data, self.basePath + file_name)

        self.testExcelSuite.remove_document(self.basePath + file_name)

    def test_get_document(self):
        file_name = "testGetDocument.xlsx"
        self.testExcelSuite.create_document(file_name)
        self.testExcelSuite.save_document()
        self.document = self.testExcelSuite.get_document(file_name)

        self.assert_document_type()

        self.testExcelSuite.remove_document(file_name)

    def test_create_document(self):
        file_name = "testCreateDocument.xlsx"
        self.testExcelSuite.create_document(file_name)
        self.testExcelSuite.save_document()
        self.testExcelSuite.add_worksheet()

        self.assert_new_file_is_empty(file_name)

        self.testExcelSuite.remove_document(file_name)

    def test_remove_document(self):
        file_name = "testRemoveDocument.xlsx"
        self.testExcelSuite.create_document(file_name)
        self.testExcelSuite.save_document()

        self.testExcelSuite.remove_document(file_name)

        self.assert_file_not_found(file_name)

    def assert_document_contains(self, value, row, column, file_name):
        self.assertEqual(value, self.testExcelSuite.read_cell_data(row, column, file_name))

    def assert_document_contains_data(self, data, file_name):
        row_number = 0
        column_number = 0
        for row in data:
            for value in row:
                self.assert_document_contains(value, row_number, column_number, file_name)
                self.column_number += 1
            column_number = 0
            row_number += 1

    def assert_file_not_found(self, file_name):
        try:
            self.testExcelSuite.get_document(file_name)
        except FileNotFoundError:
            self.assertTrue(True)
        else:
            self.assertTrue(False)

    def assert_new_file_is_empty(self, file_name):
        self.assertIsNone(self.testExcelSuite.read_cell_data(0, 0, file_name))

    def assert_document_type(self):
        self.assertEqual("Workbook", type(self.document).__name__)

if __name__ == '__main__':
    unittest.main()
