import unittest

from l0017_letter_combinations_of_a_phone_number import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(
            set([]), 
            set(Solution().letterCombinations('')))
        self.assertEqual(
            set(['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']), 
            set(Solution().letterCombinations('23')))