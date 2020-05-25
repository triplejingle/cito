from PythonExecuter import PythonExecuter

class ExecuterFactory(object):
    @staticmethod
    def get_Executer(file_extension):
        if file_extension == "py":
            return PythonExecuter()
        else:
            raise ValueError(format)
