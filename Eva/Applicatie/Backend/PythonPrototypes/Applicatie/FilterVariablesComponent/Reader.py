import openpyxl

class ExcelReader(object):

    def read_content(self, bestand):
        content = []
        row_number = 0
        self.book = openpyxl.load_workbook(bestand)
        self.sheet = self.book.active
        current_row = self.read_row(row_number)
        while len(current_row) > 0:
            content.append(current_row)
            row_number += 1
            current_row = self.read_row(row_number)
        return content

    def read_row(self, row_number):
        row = []
        column_number = 0
        current_value = self.read_cell_data(row_number, column_number, self.sheet)
        while current_value != None:
            row.append(current_value)
            column_number += 1
            current_value = self.read_cell_data(row_number, column_number, self.sheet)
        return row

    def read_cell_data(self, row, column, sheet):
        return sheet.cell(row + 1, column + 1).value
