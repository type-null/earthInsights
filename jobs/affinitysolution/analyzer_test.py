
import unittest
import analyzer

class TestMyModule(unittest.TestCase):

    def setUp(self): # run before test runs
        return # do nothing
    
    def test_do_divide(self):
        arg1 = 4
        arg2 = 2

        result = class_example.do_divide(arg1, arg2)

        expectedResult = 2

        self.assertEqual(result, expectedResult)