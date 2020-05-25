from ReaderFactory import ReaderFactory
from Niveau import Niveau

class Bestand(object):
    niveaus = []
    bestand_factory = ReaderFactory()

    def __init__(self):
        self.index_list = []

    def get_filter_criteria(self):
        filtered_niveaus = {}
        for niveau in self.niveaus:
            filtered_niveaus[niveau.name] = niveau.filtered_criteria
        return filtered_niveaus

    def filter(self, niveaus_and_variabelen):
        self.index_list = []
        niveaus = self.get_niveaus(niveaus_and_variabelen)
        for niveau in niveaus:
            variabelen = self.get_variables(niveau.name, niveaus_and_variabelen)
            indexes = niveau.filter(variabelen)
            for index in indexes:
                self.index_list.append(index)
        self.remove_single_indexes(len(niveaus))
        self.remove_duplicate_indexes()
        return self.index_list

    def remove_single_indexes(self, number_of_niveaus):
        index_list = []
        self.index_list.sort()
        for i in range(0, len(self.index_list)):
            row_number = self.index_list[i]
            if row_number in index_list:
                continue
            count_occurence = self.index_list.count(row_number)
            if count_occurence == number_of_niveaus:
                index_list.append(row_number)
        self.index_list = index_list

    def remove_duplicate_indexes(self):
        tmp = list(dict.fromkeys(self.index_list))
        tmp.sort()
        self.index_list = tmp

    def get_niveaus(self, niveau_and_variabelen):
        niveaus = []
        for x in niveau_and_variabelen:
            for niveau in self.niveaus:
                if niveau.name == x:
                    niveaus.append(niveau)
        return niveaus

    def load(self, bestand):
        self.niveaus = []
        file_type = self.get_file_type(bestand)
        self.file_reader = self.bestand_factory.get_file_reader(file_type)
        content = self.file_reader.read_content(bestand)
        niveaus = self.load_niveaus(content)
        for niveau in niveaus:
            niveau_object = Niveau()
            niveau_object.create_niveau(content, niveau)
            self.niveaus.append(niveau_object)
        return self.niveaus

    def load_niveaus(self, content):
        return content[0]

    def get_variables(self, niveau, niveau_and_variables):
        variabelen = []
        for x in niveau_and_variables[niveau]:
            variabelen.append(x)
        return variabelen

    def get_file_type(self, bestand):
        file_type = bestand.split(".")
        last_element = len(file_type)-1
        return file_type[last_element]
