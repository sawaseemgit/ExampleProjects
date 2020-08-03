import unittest
import testscript


class Testmain(unittest.TestCase):
    def setUp(self):
        print('Testing a test function')
    
    def testFn(self):
        param = 50
        result = script.Do(param)
        self.assertEqual(result, 60)

    def testFn1(self):
        """HIII"""
        param = 0
        result = script.Do(param)
        self.assertEqual(result, 'Please enter a number')


unittest.main()  # This runs all funcs defined in unittest file
