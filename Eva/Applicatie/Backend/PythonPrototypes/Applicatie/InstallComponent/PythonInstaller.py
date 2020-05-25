import os
from os import listdir
from os.path import isfile

from ScriptConfig import ScriptConfig


class PythonInstaller(object):
    script_config = ScriptConfig()

    def install(self, eigenschap):
        self.upgradePip()
        self.installTarball()
        self.installLocalLibrary(eigenschap)
        print(self.getFilesFromDirectory(self.script_config.get_location()))

    def upgradePip(self):
        os.system("python -m pip install --upgrade pip")

    def installTarball(self):
        os.system("pip install download-tarball")

    def installLocalLibrary(self, eigenschap):
        libraryPath = self.script_config.get_location() + "/" + os.path.splitext(eigenschap)[0] + "/Libraries/"
        libraries = self.getFilesFromDirectory(libraryPath)
        for library in libraries:
            os.system("pip install \"" + libraryPath + library + "/\"")

    def getFilesFromDirectory(self, scriptPath):
        fileList = []
        for file in listdir(scriptPath):
            if isfile(scriptPath + file):
                fileList.append(file)
        return fileList
