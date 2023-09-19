import unittest
import testing

class TestTesting(unittest.TestCase)
    def setUp(self):
        print('about to test a function')

    def test_do_stuff(self):
        test_param = 10
        result = testing.do_stuff(test_param)
        self.assertEqual(result, 15)
        # check that these are equal

    def test_do_stuff2(self):
        test_param = 'hjgjgjhg'
        result = testing.do_stuff(test_param)
        self.assertIsInstance(result, ValueError)

    def test_do_stuff3(self):
        test_param = None
        result = testing.do_stuff(test_param)
        self.assertIsInstance(result, 'please enter number')

    def test_do_stuff4(self):
        test_param = ''
        result = testing.do_stuff(test_param)
        self.assertIsInstance(result, 'please enter number')

    def tearDown(self):
        print('cleaning up')

if __name__ == '__main__'
    unittest.testing()

# why is this useful? - you have more than one file and each module tested
# ideally you want all of these tests run in unison
# python3 -m unittest -v
# -v = verbose (Which tests have we run and which are ok and which have failed)

# setup will run before each function
