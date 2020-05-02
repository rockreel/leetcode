import unittest

from l0288_unique_word_abbreviation import ValidWordAbbr

class Test(unittest.TestCase):
    
    def test_solution(self):
        wa = ValidWordAbbr([ "deer", "door", "cake", "card" ])
        self.assertEqual(False, wa.isUnique('dear'))
        self.assertEqual(True, wa.isUnique('cart'))
        self.assertEqual(False, wa.isUnique('cane'))
        self.assertEqual(True, wa.isUnique('make'))