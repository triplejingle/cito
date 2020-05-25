from unittest import TestCase

from mockito import when

from Script import Script
from ScriptConfig import ScriptConfig


class TestScript(TestCase):

    def test_get_properties(self):
        expected_result = ["aantalWoorden.py","Woordsoorten.py"]
        script = self.setup_test()

        result = script.get_properties()

        self.assertEqual(expected_result,result)

    def setup_test(self):
        script = Script()
        script_config = ScriptConfig()
        when(script_config).get_location().thenReturn("./testFiles/")
        script.script_config = script_config

        return script
    def runTest(self):
        self.test_get_properties()
