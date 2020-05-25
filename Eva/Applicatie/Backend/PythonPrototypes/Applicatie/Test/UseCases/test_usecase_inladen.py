import unittest

from Applicatie.Test.Inladen.test_controller import TestController
from Applicatie.Test.Inladen.test_inladen_AVLTree import Test_AVLTree
from Applicatie.Test.Inladen.test_inladen_bestand import Test_Bestand
from Applicatie.Test.Inladen.test_inladen_niveau import Test_niveau


class MyTestCase(unittest.TestCase):

    # 1 unit tests
    def test_inladen_responses_backend(self):
        test_suite = unittest.TestSuite()
        test_suite.addTest(Test_AVLTree())
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

    # 3 end to end tests
    def test_inladen_responses_end_to_end(self):
        print("hallo")


if __name__ == '__main__':
    unittest.main()
