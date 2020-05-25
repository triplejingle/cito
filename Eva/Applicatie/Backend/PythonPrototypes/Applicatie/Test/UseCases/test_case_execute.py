import unittest

from test_pythonExecuter import TestPythonExecuter


class MyTestCase(unittest.TestCase):

    # 1 unit tests
    def test_Execute(self):
        test_suite = unittest.TestSuite()
        test_suite.addTest(TestPythonExecuter())
        result = unittest.TextTestRunner(verbosity=2).run(test_suite)
        number_of_errors = 0
        self.assertEqual(number_of_errors, len(result.errors))


if __name__ == '__main__':
    unittest.main()
