import unittest

import sys
sys.path.append('../')

from match import match


class Test(unittest.TestCase):
    def test_match_one(self):
        '''
        Test that the regex and string
        are equal
        '''
        regex1 = "a.b"
        string1 = "b"
        result = match(regex1, string1)
        self.assertFalse(result)

    def test_match_two(self):
        regex2 = "a.b"
        string2 = "b"
        result = match(regex2, string2)
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
