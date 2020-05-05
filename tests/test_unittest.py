# Jack McNamee
# Testing class for this program using unittest

import unittest

import sys
sys.path.append('../')

from match import match

'''
Test that the output of matching 
regex and string is true (assertTrue)
'''
class TestClassA(unittest.TestCase):
    def test_match(self):
        regex = "(a*.b*)|a.b"
        string = "aaabbb"
        result = match(regex, string)
        self.assertTrue(result)
        pass

class TestClassB(unittest.TestCase):
    def test_match(self):
        regex = "a+.b*"
        string = "aaabbb"
        result = match(regex, string)
        self.assertTrue(result)
        pass

class TestClassC(unittest.TestCase):
    def test_match(self):
        regex = "a*|b?"
        string = "aaabbb"
        result = match(regex, string)
        self.assertTrue(result)
        pass

# runs all tests
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromModule(sys.modules[__name__])
    unittest.TextTestRunner(vebosity=2).run(suite)
