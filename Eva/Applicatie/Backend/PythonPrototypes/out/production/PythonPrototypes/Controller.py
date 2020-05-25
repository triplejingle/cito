from Bestand import Bestand


class Controller(object):
    bestand = Bestand()

    def inladen(self, path):
        return self.bestand.load(path)

    def get_criteria(self):
        return self.bestand.get_filter_criteria()

    def filter(self, niveau_en_variabelen):
        return self.bestand.filter(niveau_en_variabelen)
