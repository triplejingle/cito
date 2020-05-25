from PythonInstaller import PythonInstaller


class InstallerFactory(object):
    @staticmethod
    def get_installer(file_extension):
        if file_extension == "py":
            return PythonInstaller()
        else:
            raise ValueError(format)
