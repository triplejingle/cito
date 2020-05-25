import importlib
import os
from os import listdir
from os.path import isfile

from ScriptConfig import ScriptConfig
import base64

class PythonExecuter(object):
    script_config = ScriptConfig()

    def get_module(self, desired_module):
        script_path = self.script_config.get_location()
        directory_name = self.script_config.get_directory_name()
        module_path = script_path + "/" + os.path.splitext(desired_module)[0]
        files = self.get_files_from_directory(module_path + "/")
        module = None

        for file in files:
            if (desired_module == file):
                try:
                    module = importlib.import_module(directory_name + "." + os.path.splitext(file)[0])
                    importlib.reload(module)
                except Exception as e:
                    raise Exception(e)
                break
        return module

    def execute(self, data, eigenschap):
        script_path = self.script_config.get_location()
        module = self.get_module(eigenschap)
        function = self.get_function(module)
        if function is not None:
            function(data)
        imageDirectory = script_path + "/" + os.path.splitext(eigenschap)[0] + "/result/"
        file = self.get_files_from_directory(imageDirectory)
        return base64.b64encode(open(imageDirectory + file[0], "rb").read()).decode('utf-8')

    def get_files_from_directory(self, directory):
        fileList = []
        for file in listdir(directory):
            if isfile(directory + file):
                fileList.append(file)
        return fileList

    def get_class(self, module):
        if hasattr(module, "class_name"):
            loaded_class = getattr(module, module.class_name)
            return loaded_class
        return None

    def get_function(self, module):
        module = self.get_class(module)
        if hasattr(module, "function_name"):
            function = getattr(module, module.function_name)
            return function
        return None
