import unittest
import testing

class TestTesting(unittest.TestCase)
    def test_do_stuff(self):
        test_param = 10
        result = testing.do_stuff(test_param)
        self.assertEqual(result, 15)
        # check that these are equal

    def test_do_stuff2(self):
        test_param = 'hjgjgjhg'
        result = testing.do_stuff(test_param)
        self.assertTrue(isinstance(result, ValueError))

unittest.testing()

