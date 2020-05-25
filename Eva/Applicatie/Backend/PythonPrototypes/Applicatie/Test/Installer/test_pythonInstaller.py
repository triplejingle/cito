from unittest import TestCase

from mockito import when

from PythonInstaller import PythonInstaller
from ScriptConfig import ScriptConfig


class TestPythonInstaller(TestCase):

    def test_getFilesFromDirectory(self):
        installer = self.setup_test()
        expectedResult = ["test1.py", "aantalWoorden.py"]

        files = installer.getFilesFromDirectory("./testFiles/")

        for i in range(0, len(files)):
            self.assertEqual(expectedResult[i], files[i])

    def test_installLocalLibraries(self):
        installer = self.setup_test()

        try:
            installer.installLocalLibrary("test1.py")
        except:
            self.assertTrue(False)

    def test_upgradePip(self):
        installer = self.setup_test()

        try:
            installer.upgradePip()
        except:
            self.assertTrue(False)
        self.assertTrue(True)

    def test_install_tarball(self):
        installer = self.setup_test()

        try:
            installer.installTarball()
        except:
            self.assertTrue(False)
        self.assertTrue(True)

    def setup_test(self):
        executer = PythonInstaller()
        script_config = ScriptConfig()
        when(script_config).get_location().thenReturn("./testFiles")
        when(script_config).get_max_number_of_rows().thenReturn("1")
        when(script_config).get_directory_name().thenReturn("testFiles")
        executer.script_config = script_config

        return executer
    def runTest(self):
        self.test_getFilesFromDirectory()
        self.test_install_tarball()
        self.test_installLocalLibraries()
        self.test_upgradePip()
