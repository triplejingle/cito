from AVLtree import AVLTree


class Niveau(object):
    def __init__(self):
        self.indexes = []
        self.filtered_criteria = []
        self.variabelen = AVLTree()
        self.name = ""

    def create_niveau(self, content, niveau):
        self.name = niveau
        column_number = self.get_column_index(content)
        variabelen = self.get_variables(column_number, content)
        increment = 0
        for variable in variabelen:
            self.add(variable, increment)
            increment += 1
        self.set_filter_criteria(column_number, content)

    def filter(self, variabelen):
        self.indexes = []
        for variable in variabelen:
            indexes = self.search(variable)
            self.add_indexes_to_filtered_list(indexes)
        return self.indexes

    def get_variables(self, column_number, content):
        variabelen = []
        var = iter(content)
        next(var)
        for row in var:
            if row is None:
                continue
            variabelen.append(row[column_number])
        return variabelen

    def get_column_index(self, content):
        column_number = 0
        for column in content[column_number]:
            if column == self.name:
                break
            column_number += 1
        return column_number

    def add(self, variable, increment):
        if self.variabelen.root is None:
            root = self.variabelen.insert(None, variable, increment)
            self.variabelen.root = root
            return
        root = self.variabelen.root
        root = self.variabelen.insert(root, variable, increment)
        self.variabelen.root = root

    def set_filter_criteria(self, column_number, content):
        var = iter(content)
        next(var)
        for row in var:
            if row[column_number] is None:
                continue
            if row[column_number] not in self.filtered_criteria:
                self.filtered_criteria.append(row[column_number])

    def search(self, variable):
        index = self.variabelen.find(variable).value
        return index

    def add_indexes_to_filtered_list(self, indexes):
        for index in indexes:
            self.indexes.append(index)
