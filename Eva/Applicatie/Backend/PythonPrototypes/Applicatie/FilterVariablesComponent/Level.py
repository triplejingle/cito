from AVLtree import AVLTree


class Level(object):
    def __init__(self):
        self.row_numbers = []
        self.filtered_criteria = []
        self.variables = AVLTree()
        self.name = ""

    def create_level(self, content, level):
        self.name = level
        column_number = self.get_column_index(content)
        variables = self.get_variables(column_number, content)
        increment = 1
        for variable in variables:
            self.add(str(variable), increment)
            increment += 1
        self.set_filter_criteria(column_number, content)

    def filter(self, variables):
        self.row_numbers = []
        for variable in variables:
            row_numbers = self.search(variable)
            self.add_row_numbers_to_filtered_list(row_numbers)
        return self.row_numbers

    def get_variables(self, column_number, content):
        variables = []
        var = iter(content)
        next(var)
        for row in var:
            total_number_of_columns = len(row) - 1
            if row is None or column_number > total_number_of_columns:
                continue
            variables.append(str(row[column_number]))
        return variables

    def get_column_index(self, content):
        column_number = 0
        for column in content[column_number]:
            if column == self.name:
                break
            column_number += 1
        return column_number

    def add(self, variable, increment):
        if self.variables.root is None:
            root = self.variables.insert(None, variable, increment)
            self.variables.root = root
            return
        root = self.variables.root
        root = self.variables.insert(root, variable, increment)
        self.variables.root = root

    def set_filter_criteria(self, column_number, content):
        var = iter(content)
        next(var)

        for row in var:
            number_of_elements = len(row) - 1
            if column_number > number_of_elements:
                continue
            if row[column_number] is None:
                continue
            if row[column_number] not in self.filtered_criteria:
                self.filtered_criteria.append(row[column_number])

    def search(self, variable):
        index = self.variables.find(str(variable)).value
        return index

    def add_row_numbers_to_filtered_list(self, indexes):
        for index in indexes:
            self.row_numbers.append(index)
