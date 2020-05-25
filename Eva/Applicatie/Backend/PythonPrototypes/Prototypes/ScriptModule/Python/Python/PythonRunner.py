import importlib
import os
import subprocess
import sys
from os import listdir
from os.path import isfile

# Waarom geen install()
#
from pkg_resources import DistributionNotFound, VersionConflict

scriptPath = "./scripts/"
script = "scripts."

def loadModule(desiredModule):
    scriptPath = "./scripts/"
    fileList = getFilesFromDirectory(scriptPath)
    return getModule(desiredModule, fileList)


def getModule(desiredModule, fileList):
    module = None
    for f in fileList:
        if (desiredModule == os.path.splitext(f)[0]):
            try:
                module = importlib.import_module(script + os.path.splitext(f)[0])
                importlib.reload(module)
            except ImportError as error:
                errorNumber = install(error.name)
                if (errorNumber == 0):
                    print("can't run script maybe try another version of the library:" + error.name)
                    break
                loadModule(desiredModule)
            except DistributionNotFound:
                raise Exception(DistributionNotFound)
            except VersionConflict as error:
                install(str(error.req))
            break
    return module


# import sys
# sys.path.append('my/path/to/module/folder')
# import module-of-interest
def getFilesFromDirectory(scriptPath):
    fileList = []
    for file in listdir(scriptPath):
        if isfile(scriptPath + file):
            fileList.append(file)
    return fileList


def executeFunction(module):
    result = getattr(module, module.decoratedFunction)
    print(result())


def install(package):
    try:
        return subprocess.check_call([sys.executable, "-m", "pip", "install", package])
    except VersionConflict:
        print(VersionConflict)


if __name__ == "__main__":
    while (True):
        try:
            module = loadModule("GithubPrototype")
            if module is not None:
                executeFunction(module)
        except ValueError:
            print(ValueError)
