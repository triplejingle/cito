from unittest import TestCase

from mockito import when, unstub

from PythonExecuter import PythonExecuter
from ScriptConfig import ScriptConfig


class TestPythonExecuter(TestCase):

    def test_getModule(self):
        executer = self.setup_test()

        expectedResult = "testFiles.test1"

        module = executer.get_module("test1.py")

        self.assertEqual(expectedResult, module.__name__)
        unstub()

    def test_execute_with_class(self):
        executer = self.setup_test()

        try:
            executer.execute("data", "test1.py")
        except:
            self.assertTrue(False)

        self.assertTrue(True)

    def test_execute_with_function(self):
        executer = self.setup_test()

        try:
            executer.execute("data", "aantalWoorden.py")
        except:
            self.assertTrue(False)

        self.assertTrue(True)

    def test_execute_with_no_function_or_class(self):
        executer = self.setup_test()

        try:
            executer.execute("data", "Woordsoorten.py")
        except:
            self.assertTrue(False)

        self.assertTrue(True)

    def setup_test(self):
        executer = PythonExecuter()
        script_config = ScriptConfig()
        when(script_config).get_location().thenReturn("./testFiles")
        when(script_config).get_max_number_of_rows().thenReturn("1")
        when(script_config).get_directory_name().thenReturn("testFiles")
        executer.script_config = script_config

        return executer
    def runTest(self):
        self.test_execute_with_class()
        self.test_execute_with_function()
        self.test_execute_with_no_function_or_class()
        self.test_getModule()
