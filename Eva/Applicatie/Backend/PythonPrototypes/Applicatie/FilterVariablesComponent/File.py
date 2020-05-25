from Level import Level
from ReaderFactory import ReaderFactory


class File(object):
    file_factory = ReaderFactory()
    file_content = {}

    def __init__(self):
        self.levels = []
        self.filtered_list = []

    def load(self, file):
        file_type = self.get_file_type(file)
        self.file_reader = self.file_factory.get_file_reader(file_type)
        content = self.file_reader.read_content(file)
        self.set_rows(content)
        return self.extract_levels_from_content(file)

    def set_rows(self, content):
        var = iter(content)
        next(var)
        increment = 1
        for row in var:
            if row is None:
                continue
            variables = []
            variables.append(row)
            self.file_content[increment] = variables
            increment += 1
        return variables

    def get_filter_criteria(self):
        filtered_levels = {}
        for niveau in self.levels:
            filtered_levels[niveau.name] = niveau.filtered_criteria
        return filtered_levels

    def filter(self, filter_criteria):
        self.filtered_list = []
        levels = self.get_levels(filter_criteria)
        for level in levels:
            variables = self.get_variables(level.name, filter_criteria)
            row_numbers = level.filter(variables)
            for row_number in row_numbers:
                self.filtered_list.append(row_number)
        self.remove_single_row_numbers(len(levels))
        self.remove_duplicate_row_numbers()
        filter_results = [{}]

        levels = []
        for level in self.levels:
            levels.append(level.name)
        filter_results.append(levels)
        for index in self.filtered_list:
            filter_results.append(self.file_content.get(index))
        return filter_results

    def remove_single_row_numbers(self, number_of_levels):
        index_list = []
        self.filtered_list.sort()
        for i in range(0, len(self.filtered_list)):
            row_number = self.filtered_list[i]
            if row_number in index_list:
                continue
            count_occurence = self.filtered_list.count(row_number)
            if count_occurence == number_of_levels:
                index_list.append(row_number)
        self.filtered_list = index_list

    def remove_duplicate_row_numbers(self):
        tmp = list(dict.fromkeys(self.filtered_list))
        tmp.sort()
        self.filtered_list = tmp

    def get_levels(self, levels_and_variables):
        levels = []
        level_key = 'name'
        for element in levels_and_variables:
            for level in self.levels:
                if level.name == element[level_key]:
                    levels.append(level)
        return levels

    def extract_levels_from_content(self, file):
        self.levels = []
        content = self.file_reader.read_content(file)
        levels = self.load_levels(content)
        for level in levels:
            level_object = Level()
            level_object.create_level(content, level)
            self.levels.append(level_object)
        return self.levels

    def load_levels(self, content):
        return content[0]

    def get_variables(self, level, levels_and_variables):
        variables = []
        level_index = 'name'
        variables_index = 'variables'
        for element in levels_and_variables:
            if level == element[level_index]:
                variables = element[variables_index]
        return variables

    def get_file_type(self, file):
        file_type = file.split(".")
        last_element = len(file_type) - 1
        return file_type[last_element]
