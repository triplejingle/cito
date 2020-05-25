import json
import os

from ExecuterFactory import ExecuterFactory
from InstallerFactory import InstallerFactory
from ScriptConfig import ScriptConfig


class Script(object):
    installer_factory = InstallerFactory()
    executer_factory = ExecuterFactory()
    script_config = ScriptConfig()

    def execute(self, data):
        total_rows = self.get_total_rows(data)
        property = self.get_property_from_data(data)
        #if total_rows < self.script_config.get_max_number_of_rows():
        extension = self.get_file_extension(data)
        installer = self.installer_factory.get_installer(extension)
        installer.install(property)
        executer = self.executer_factory.get_Executer(extension)
        try:
            image = executer.execute(data, property)
        except Exception as error:
            raise Exception(error)
        return image
        #else:
            #print("execute on server and return that image")

    def get_file_extension(self, data):
        property = self.get_property_from_data(data)
        file_type = property.split(".")
        last_element = len(file_type) - 1
        return file_type[last_element]

    def get_total_rows(self, data):
        total_rows = 'Totalrows'
        print(json.loads(data)[total_rows])
        return json.loads(data)[total_rows]

    def get_property_from_data(self, data):
        property = 'PropertyExtractionScript'
        return json.loads(data)[property]

    def get_properties(self):
        file_names = []
        for directory in os.listdir(self.script_config.get_location()):
            script_path =self.script_config.get_location()+directory
            for file in os.listdir(script_path):
                if os.path.isfile(script_path+"/"+file):
                    file_names.append(file)
        return file_names
