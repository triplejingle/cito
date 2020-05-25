import unittest

from test_pythonInstaller import TestPythonInstaller


class MyTestCase(unittest.TestCase):

    # 1 unit tests
    def test_inladen_responses_backend(self):
        test_suite = unittest.TestSuite()
        test_suite.addTest(TestPythonInstaller())
        result = unittest.TextTestRunner(verbosity=2).run(test_suite)
        number_of_errors = 0
        self.assertEqual(number_of_errors, len(result.errors))


if __name__ == '__main__':
    unittest.main()
