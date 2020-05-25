import json

from File import File
from Script import Script


class VisualizeVariablesController(object):
    file = File()
    script = Script()

    def load(self, path):
        return self.file.load(path)
    def get_criteria(self):
        return self.file.get_filter_criteria()

    def filter(self, levels_and_variables):
        return self.file.filter(json.loads(levels_and_variables))

    def get_properties(self):
        return self.script.get_properties()

    def execute(self, data):
        return self.script.execute(data)
