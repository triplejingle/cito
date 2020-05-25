import unittest

from test_filteren_bestand import Test_Bestand
from test_filteren_controller import TestController
from test_filteren_niveau import Test_niveau


class MyTestCase(unittest.TestCase):

    # 1 unit tests
    def test_inladen_responses_backend(self):
        test_suite = unittest.TestSuite()
        test_suite.addTest(Test_Bestand())
        test_suite.addTest(Test_niveau())
        result = unittest.TextTestRunner(verbosity=2).run(test_suite)
        number_of_errors = 0
        self.assertEqual(number_of_errors, len(result.errors))

    # 2 integratie test
    def test_inladen_responses_integratie_test(self):
        test_suite = unittest.TestSuite()
        test_suite.addTest(TestController())
        result = unittest.TextTestRunner(verbosity=2).run(test_suite)
        number_of_errors = 0
        self.assertEqual(number_of_errors, len(result.errors))

if __name__ == '__main__':
    unittest.main()
